import sys

from .. import *
from . import *

exit = False
if "light" in status:
    printErr("command line interface not available in light version")
    exit = True

if __name__ == "__main__" and not exit:
    localRepo = False
    action = None
    value = None
    pList = False
    iList = False
    eList = False
    fList = "txt"
    smart = False
    export = False
    for a in sys.argv[1:]:
        if action == "update" and ("--export" in a or "-e" in a):
            if ":" in a:
                eList = a.split(":")[1]
            else:
                eList = True
        elif action == "update" and ("--import" in a or "-i" in a):
            if ":" in a:
                iList = a.split(":")[1]
            else:
                iList = True
        elif action == "update" and ("--format" in a or "-f" in a):
            fList = "py"
        elif "--list" in a and not pList:
            if ":" in a:
                pList = a.split(":")[1]
            else:
                pList = True
        elif "--local" in a or "-l" in a and not localRepo:
            if ":" in a:
                localRepo = a.split(":")[1]
            else:
                localRepo = True
        elif "--smart" in a or "-s" in a and not smart:
            if ":" in a:
                smart = a.split(":")[1]
            else:
                smart = True
        elif "--export" in a or "-e" in a and not export:
            if ":" in a:
                export = a.split(":")[1]
            else:
                export = True
        elif a in ["search", "s"] and not action:
            action = "search"
        elif a in ["install", "i"] and not action:
            action = "install"
        elif a in ["download", "d"] and not action:
            action = "download"
        elif a in ["wheel", "w"] and not action:
            action = "wheel"
        elif a in ["update", "u"] and not action:
            action = "update"
        elif a in ["version", "v"] and not action:
            action = "version"
        else:
            if value is None:
                value = ""
            if value:
                value += " "
            value += a

    if action == "update":
        updateBuiltinList(eList, iList, fList)
    else:
        main(
            action, value=value, local=localRepo, list=pList, smart=smart, export=export
        )
