import functools
from asyncio import get_event_loop
from typing import Any, Callable, List, Optional, Tuple, TypeVar

from prot.prompt.application import Application
from prot.prompt.application.current import get_app
from prot.prompt.buffer import Buffer
from prot.prompt.completion import Completer
from prot.prompt.eventloop import run_in_executor_with_context
from prot.prompt.filters import FilterOrBool
from prot.prompt.formatted_text import AnyFormattedText
from prot.prompt.key_binding.bindings.focus import focus_next, focus_previous
from prot.prompt.key_binding.defaults import load_key_bindings
from prot.prompt.key_binding.key_bindings import KeyBindings, merge_key_bindings
from prot.prompt.layout import Layout
from prot.prompt.layout.containers import AnyContainer, HSplit
from prot.prompt.layout.dimension import Dimension as D
from prot.prompt.styles import BaseStyle
from prot.prompt.widgets import (
    Box,
    Button,
    CheckboxList,
    Dialog,
    Label,
    ProgressBar,
    RadioList,
    TextArea,
)

__all__ = [
    "yes_no_dialog",
    "button_dialog",
    "input_dialog",
    "message_dialog",
    "radiolist_dialog",
    "checkboxlist_dialog",
    "progress_dialog",
]


def yes_no_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    yes_text: str = "Yes",
    no_text: str = "No",
    style: Optional[BaseStyle] = None,
) -> Application[bool]:
    """
    Display a Yes/No dialog.
    Return a boolean.
    """

    def yes_handler() -> None:
        get_app().exit(result=True)

    def no_handler() -> None:
        get_app().exit(result=False)

    dialog = Dialog(
        title=title,
        body=Label(text=text, dont_extend_height=True),
        buttons=[
            Button(text=yes_text, handler=yes_handler),
            Button(text=no_text, handler=no_handler),
        ],
        with_background=True,
    )

    return _create_app(dialog, style)


_T = TypeVar("_T")


def button_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    buttons: List[Tuple[str, _T]] = [],
    style: Optional[BaseStyle] = None,
) -> Application[_T]:
    """
    Display a dialog with button choices (given as a list of tuples).
    Return the value associated with button.
    """

    def button_handler(v: _T) -> None:
        get_app().exit(result=v)

    dialog = Dialog(
        title=title,
        body=Label(text=text, dont_extend_height=True),
        buttons=[
            Button(text=t, handler=functools.partial(button_handler, v))
            for t, v in buttons
        ],
        with_background=True,
    )

    return _create_app(dialog, style)


def input_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "OK",
    cancel_text: str = "Cancel",
    completer: Optional[Completer] = None,
    password: FilterOrBool = False,
    style: Optional[BaseStyle] = None,
) -> Application[str]:
    """
    Display a text input box.
    Return the given text, or None when cancelled.
    """

    def accept(buf: Buffer) -> bool:
        get_app().layout.focus(ok_button)
        return True  # Keep text.

    def ok_handler() -> None:
        get_app().exit(result=textfield.text)

    ok_button = Button(text=ok_text, handler=ok_handler)
    cancel_button = Button(text=cancel_text, handler=_return_none)

    textfield = TextArea(
        multiline=False, password=password, completer=completer, accept_handler=accept
    )

    dialog = Dialog(
        title=title,
        body=HSplit(
            [Label(text=text, dont_extend_height=True), textfield,],
            padding=D(preferred=1, max=1),
        ),
        buttons=[ok_button, cancel_button],
        with_background=True,
    )

    return _create_app(dialog, style)


def message_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "Ok",
    style: Optional[BaseStyle] = None,
) -> Application[None]:
    """
    Display a simple message box and wait until the user presses enter.
    """
    dialog = Dialog(
        title=title,
        body=Label(text=text, dont_extend_height=True),
        buttons=[Button(text=ok_text, handler=_return_none),],
        with_background=True,
    )

    return _create_app(dialog, style)


def radiolist_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    style: Optional[BaseStyle] = None,
) -> Application[_T]:
    """
    Display a simple list of element the user can choose amongst.

    Only one element can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=radio_list.current_value)

    radio_list = RadioList(values)

    dialog = Dialog(
        title=title,
        body=HSplit(
            [Label(text=text, dont_extend_height=True), radio_list,], padding=1
        ),
        buttons=[
            Button(text=ok_text, handler=ok_handler),
            Button(text=cancel_text, handler=_return_none),
        ],
        with_background=True,
    )

    return _create_app(dialog, style)


def checkboxlist_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    ok_text: str = "Ok",
    cancel_text: str = "Cancel",
    values: Optional[List[Tuple[_T, AnyFormattedText]]] = None,
    style: Optional[BaseStyle] = None,
) -> Application[List[_T]]:
    """
    Display a simple list of element the user can choose multiple values amongst.

    Several elements can be selected at a time using Arrow keys and Enter.
    The focus can be moved between the list and the Ok/Cancel button with tab.
    """
    if values is None:
        values = []

    def ok_handler() -> None:
        get_app().exit(result=cb_list.current_values)

    cb_list = CheckboxList(values)

    dialog = Dialog(
        title=title,
        body=HSplit([Label(text=text, dont_extend_height=True), cb_list,], padding=1),
        buttons=[
            Button(text=ok_text, handler=ok_handler),
            Button(text=cancel_text, handler=_return_none),
        ],
        with_background=True,
    )

    return _create_app(dialog, style)


def progress_dialog(
    title: AnyFormattedText = "",
    text: AnyFormattedText = "",
    run_callback: Callable[[Callable[[int], None], Callable[[str], None]], None] = (
        lambda *a: None
    ),
    style: Optional[BaseStyle] = None,
) -> Application[None]:
    """
    :param run_callback: A function that receives as input a `set_percentage`
        function and it does the work.
    """
    loop = get_event_loop()
    progressbar = ProgressBar()
    text_area = TextArea(
        focusable=False,
        # Prefer this text area as big as possible, to avoid having a window
        # that keeps resizing when we add text to it.
        height=D(preferred=10 ** 10),
    )

    dialog = Dialog(
        body=HSplit(
            [Box(Label(text=text)), Box(text_area, padding=D.exact(1)), progressbar,]
        ),
        title=title,
        with_background=True,
    )
    app = _create_app(dialog, style)

    def set_percentage(value: int) -> None:
        progressbar.percentage = int(value)
        app.invalidate()

    def log_text(text: str) -> None:
        loop.call_soon_threadsafe(text_area.buffer.insert_text, text)
        app.invalidate()

    # Run the callback in the executor. When done, set a return value for the
    # UI, so that it quits.
    def start() -> None:
        try:
            run_callback(set_percentage, log_text)
        finally:
            app.exit()

    def pre_run() -> None:
        run_in_executor_with_context(start)

    app.pre_run_callables.append(pre_run)

    return app


def _create_app(dialog: AnyContainer, style: Optional[BaseStyle]) -> Application[Any]:
    # Key bindings.
    bindings = KeyBindings()
    bindings.add("tab")(focus_next)
    bindings.add("s-tab")(focus_previous)

    return Application(
        layout=Layout(dialog),
        key_bindings=merge_key_bindings([load_key_bindings(), bindings,]),
        mouse_support=True,
        style=style,
        full_screen=True,
    )


def _return_none() -> None:
    " Button handler that returns None. "
    get_app().exit()
