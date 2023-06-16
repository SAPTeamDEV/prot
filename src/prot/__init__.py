import builtins as _builtins
import hashlib as _hashlib
import os as _os
import py_compile as _py_compile
import random as _random
import runpy as _r
import socket as _socket
import sys as _sys
import threading as _threading
import time as _time
from time import sleep as _sleep

try:
    from docutils.core import publish_file as _pf
except:
    _pf = None
try:
    import colorama as _c

    Fore = _c.ansi.Fore
    Back = _c.ansi.Back
    Style = _c.ansi.Style
    clear_line = _c.ansi.clear_line
    clear_screen = _c.ansi.clear_screen
    outWin32 = _c.ansitowin32.AnsiToWin32(_sys.stdout, convert=True)
    _c = True
except:
    _c = False

__all__ = ["status"]

try:
    from . import __version__ as _ver

    __version__ = _ver.__version__
except:
    pass

if hasattr(_sys, "runningPPF"):
    PyProtFramework = True
else:
    PyProtFramework = False

status = []

if not _os.path.split(_os.path.split(__file__)[0])[1] == "prot":
    status.append("unofficial")
else:
    status.append("official")

if _os.path.split(_os.path.split(__file__)[0])[1] in ["lightprot", "protbuilder"]:
    status.append("light")
    try:
        _prt = __import__("prot")
        status.append("haveProt")
    except:
        _prt = None

Empty = "empty"

nameDict = {
    "printMsg": "print",
    "insertColor": "applycolors",
    "cleanColor": "removecolors",
    "getRandomString": "randomstring",
    "checkFileSame": "checkfilesame",
    "runAsMain": "runmoduleasmain",
}

colors = {
    "foreground": {
        "black": Fore.BLACK,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
        "reset": Fore.RESET,
    },
    "background": {
        "black": Back.BLACK,
        "red": Back.RED,
        "green": Back.GREEN,
        "yellow": Back.YELLOW,
        "blue": Back.BLUE,
        "magenta": Back.MAGENTA,
        "cyan": Back.CYAN,
        "white": Back.WHITE,
        "reset": Back.RESET,
    },
    "style": {
        "bright": Style.BRIGHT,
        "dim": Style.DIM,
        "normal": Style.NORMAL,
        "end": Style.RESET_ALL,
        "clearline": clear_line(),
        "clear": clear_screen(),
    },
}

colorSymbols = {"foreground": "-", "background": "+", "style": "*"}

charDict = {
    "lowers": "abcdefghijklmnopqrstuvwxyz",
    "uppers": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "symbols": "./~!@#$%&*-_=+?",
    "numbers": "0123456789",
}

patterns = ["%s =", "%s=", "as %s", "import %s", "%s,"]

settingFilePath = _os.path.join(_os.path.split(__file__)[0], "settings")
databaseFilePath = _os.path.join(_os.path.split(__file__)[0], "database")

localSets = False

settingVals = {
    "repo": "default",
    "ui": "normal",
    "orderedBuiltinList": "on",
    "saveDatabase": "off",
    "colorize": "on",
    "printMsgPrefix": "",
    "printMsgColor": "",
}

settingChoices = {
    "ui": ["verysmall", "small", "normal"],
    "orderedBuiltinList": ["off", "on"],
    "colorize": ["off", "on"],
    "saveDatabase": ["off", "on"],
    "printMsgColor": [color for color in colors["foreground"]],
}

settingData = None


def prot(args=None):
    if type(args) == list:
        args = ["prot"] + args
    elif type(args) == str:
        args = ["prot"] + args.split(" ")
    else:
        args = _sys.argv
    if not args[0] == "prot":
        args[0] = "prot"
    _sys.argv = args
    _r._run_module_as_main(_sys.argv[0])


def addBuiltins(obj, name=None, checkPPF=True):
    if checkPPF and not PyProtFramework:
        return obj
    if name:
        objname = name
    else:
        objname = obj.__name__
    if objname in nameDict:
        setattr(_builtins, nameDict[objname], obj)
    else:
        setattr(_builtins, objname, obj)
    return obj


def appendAll(obj, name=None):
    global __add__
    __all__.append(name if name else obj if type(obj) == str else obj.__name__)
    return obj


@appendAll
def verifyColor(color, exceptionOnNot=True):
    for c in colors["foreground"]:
        if color == c:
            return True
    if exceptionOnNot:
        raise ValueError("color not found.")
    else:
        return False


@appendAll
@addBuiltins
def insertColor(string):
    for c in colors:
        for sc in colors[c]:
            string = string.replace(colorSymbols[c] + sc, colors[c][sc])
    return string


@appendAll
@addBuiltins
def cleanColor(string):
    for c in colors:
        for sc in colors[c]:
            string = string.replace(colorSymbols[c] + sc, "")
    return string


@appendAll
@addBuiltins
def getRandomString(Len=4, types=["lowers", "uppers", "symbols", "numbers"]):
    if not type(types) == list:
        raise TypeError("types argument must be a list object.")
    string = ""
    for r in range(Len):
        string += _random.choice(str2list(charDict[_random.choice(types)]))
    return string


@appendAll
def testSpeed(count):
    progress = Progress(
        maxVal=count,
        msgForm="($VAL/$MAX) $TIME $PERC% completed",
        replaces=[["$TIME", TimeWidget(milisec=True)]],
        inline=True,
    )
    for c in range(count):
        progress.next()
    progress.newline()


@appendAll
def getVarFromFile(file, variable):
    if type(file) == str:
        file = open(file).read()
    fileMap = file.splitlines()
    for f in fileMap:
        if f:
            for t in patterns:
                ct = t % variable
                if ct in f:

                    class tempCls:
                        exec(f)

                    res = getattr(tempCls, variable)
                    return res


@appendAll
def checkMethods(obj):
    for s in dir(obj):
        printMsg(s + " : " + str(getattr(obj, s)))


@appendAll
def callMethods(obj):
    for s in dir(obj):
        try:
            printMsg("result of " + s + "() is " + str(getattr(obj, s)()))
        except:
            printMsg("error in " + str(s) + "()")


@appendAll
def callMethodsWithArg(obj, arg):
    for s in dir(obj):
        try:
            printMsg(
                "result of " + s + "(" + str(arg) + ") is " + str(getattr(obj, s)(arg))
            )
        except:
            printMsg("error in " + str(s) + "(" + str(arg) + ")")


@appendAll
@addBuiltins
def checkFileSame(f1, f2):
    try:
        md5s = [_hashlib.md5(), _hashlib.md5()]
        fs = [f1, f2]
        for i in range(2):
            f = open(fs[i], "rb")
            block_size = 2**20
            while True:
                data = f.read(block_size)
                if not data:
                    break
                md5s[i].update(data)
            f.close()
            md5s[i] = md5s[i].hexdigest()
        return md5s[0] == md5s[1]
    except:
        return False


@appendAll
def splitStr(string, length):
    out = []
    try:
        if len(string) > length:
            splitDelay = len(string) // length
            for i in range(splitDelay):
                out.append(string[:length])
                string = string[length:]
            if not string == "":
                out.append(string)
        else:
            out = [string]
    except:
        out = []
    return out


@appendAll
def compileStr(string):
    try:
        if "." in string:
            out = float(string)
        else:
            out = int(string)
    except:
        if string in ["True", "False", "None"]:
            out = True if string == "True" else False if string == "False" else None
        else:
            out = str(string)
    return out


@appendAll
def extractStr(string):
    splittedList = string.split(",")
    splittedDict = {}
    splittedListNew = []
    for i in splittedList:
        if len(i.split(":")) > 1:
            splittedDict[i.split(":")[0]] = i.split(":")[1]
    for i in splittedList:
        if len(i.split(":")) > 1:
            for s in i.split(":"):
                splittedListNew.append(s)
        else:
            splittedListNew.append(i)
    if len(splittedListNew) == 0 and len(splittedDict) == 0:
        raise ValueError("this string is not encoded.")
    else:
        data = Database()
        for i in splittedListNew:
            data.append(i)
        for i in splittedDict:
            data[i] = splittedDict[i]
        return data


@appendAll
def pyCompile(source, usePEP=True, subfolders=False, deleteSource=False):
    if _os.path.isdir(source):
        for p in _os.listdir(source):
            if _os.path.isdir(source + "/" + p):
                if subfolders:
                    pyCompile(source + "/" + p, usePEP, subfolders, deleteSource)
            else:
                pyCompile(source + "/" + p, usePEP, deleteSource=deleteSource)
    if _os.path.exists(source):
        if source.lower().endswith(".py"):
            _py_compile.compile(
                source, cfile=None if usePEP else source + "c", optimize=2
            )
            if deleteSource:
                _os.remove(source)
    else:
        printErr("file or folder " + source + " not found.")
        return


@appendAll
@addBuiltins
def condition(string):
    exec("res = " + string)
    return res


@appendAll
@addBuiltins
def runAsMain(args=None):
    if type(args) == list:
        pass
    elif type(args) == str:
        args = args.split(" ")
    else:
        args = _sys.argv
    _sys.argv = args
    _r._run_module_as_main(_sys.argv[0])


@appendAll
@addBuiltins
def printMsg(msg="", color=None, end="\n", file=None, colorize=True, prefix=True):
    global _c
    try:
        if "light" in status and "haveProt" in status and _prt is not None:
            settings.colorize = _prt.settings.colorize
    except:
        pass
    if settings.colorize == "off" or not _sys.stdout == _sys.__stdout__:
        _c = False
    if prefix and settings.printMsgPrefix:
        msg = str(settings.printMsgPrefix) + str(msg)
    else:
        msg = str(msg)
    if color and verifyColor(color):
        msg = "-" + color + msg + "*end"
    elif settings.printMsgColor:
        msg = "-" + settings.printMsgColor + msg + "*end"
    if colorize:
        if settings.colorize == "off":
            msg = cleanColor(msg)
        elif not _os.name == "nt" or _c:
            msg = insertColor(msg)
        else:
            msg = cleanColor(msg)
    if file is None:
        if _os.name == "nt" and _c:
            out = outWin32
        else:
            out = _sys.stdout
    else:
        out = file
    out.write(msg + end)
    try:
        out.flush()
    except:
        pass


@appendAll
def printErr(msg):
    printMsg("ERROR: " + str(msg), color="red")


@appendAll
def printWarn(msg):
    printMsg("WARNING: " + str(msg), color="yellow")


@appendAll
def getLocalIP():
    sock = _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)
    try:
        sock.connect(("10.255.255.255", 1))
        ip = sock.getsockname()[0]
    except:
        ip = "127.0.0.1"
    finally:
        sock.close()
    return ip


@appendAll
def checkAvail(address, timeout=0.5):
    sock = _socket.socket()
    sock.settimeout(timeout)
    try:
        sock.connect(address)
        sock.close()
        return True
    except:
        return False


@appendAll
def getBaseAddr(address):
    return ".".join(address.split(".")[:3])


@appendAll
def netScan(port=80, timeout=0.5):
    ports = port if type(port) == list else [port]
    baseAddr = getBaseAddr(getLocalIP())
    hostsAvail = []
    for n in range(256):
        host = baseAddr + "." + str(n)
        for p in ports:
            if checkAvail((host, p), timeout):
                hostsAvail.append((host, p))
    return hostsAvail


@appendAll
def netAttack(addr, times):
    val1 = ValueWidget(" starting")
    prog = Progress(
        maxVal=times * 2, msgForm="$PERC% $MSG$1", replaces=[["$1", val1]], inline=True
    )
    for t in range(times):
        val1.value = " connecting to " + str(addr[0]) + ":" + str(addr[1])
        prog.next()
        sock = _socket.socket()
        sock.connect(addr)
        val1.value = " disconnecting from " + str(addr[0]) + ":" + str(addr[1])
        prog.next()
        sock.close()
    val1.value = ""
    prog.show()
    prog.newline()


@appendAll
@addBuiltins
class Matrix(list):
    def __getitem__(self, key):
        if type(key) == int:
            return list.__getitem__(self, key)
        else:
            res = self.get(key, default=Empty)
            if res == Empty:
                raise KeyError(key)
            return res

    def __setitem__(self, key, value):
        self._checkValue(value)
        if type(key) == int:
            list.__setitem__(self, key, value)
        else:
            self.append([key, value])

    def __init__(self, value=[]):
        try:
            if value:
                self._checkValue(value)
        except:
            for v in value:
                self._checkValue(v)
        list.__init__(self, value)

    def _checkValue(self, value):
        if type(value) in [list, tuple, Matrix] and len(value) == 2:
            return True
        raise ValueError(
            "value must be object of Matrix, list or tuple classes and should have only two members"
        )

    def append(self, value):
        self._checkValue(value)
        list.append(self, value)

    def __delitem__(self, key):
        if type(key) == int:
            list.__delitem__(self, key)
        for k in self:
            try:
                if k[0] == key:
                    self.remove(k)
            except:
                pass

    def get(self, key, default=None):
        for k in self:
            try:
                if k[0] == key:
                    return k[1]
            except:
                pass
        return default


@appendAll
def rst2html(path, subdirs=False):
    if _pf is None:
        printErr("docutils package needed.")
        return
    if _os.path.isdir(path):
        for p in _os.listdir(path):
            if _os.path.isdir(path + "/" + p):
                if subdirs:
                    rst2html(path + "/" + p, True)
            else:
                rst2html(path + "/" + p)
    if _os.path.exists(path):
        if path.endswith(".rst"):
            try:
                _pf(
                    source_path=path,
                    destination_path=path.split(".rst")[0] + ".html",
                    writer_name="html",
                )
            except:
                import traceback

                traceback.print_stack()
                traceback.print_exc()
    else:
        printErr("file or folder " + path + " not found.")
        return


@appendAll
def dict2matrix(obj):
    if not type(obj) == dict:
        raise TypeError("dict object is required.")
    matrix = []
    for m in obj:
        if type(obj[m]) == dict:
            matrix.append([m, dict2matrix(obj[m])])
        else:
            matrix.append(Matrix([m, obj[m]]))
    return Matrix(matrix)


@appendAll
def str2list(string):
    if not type(string) == str:
        raise TypeError("str object is required.")
    strList = []
    for s in string:
        strList.append(s)
    return strList


@appendAll
def list2str(listObj, space=""):
    if not type(listObj) == list:
        raise TypeError("list object is required.")
    string = ""
    for s in listObj:
        if string:
            string += space
        string += str(s)
    return string


@appendAll
def matrix2str(mat, space=""):
    if not type(mat) in [list, Matrix]:
        raise TypeError("list or Matrix object is required.")
    string = ""
    for m in mat:
        if string:
            string += space
        if type(m) in [list, Matrix]:
            string += str(matrix2str(m))
        elif type(m) == dict:
            string += str(matrix2str(dict2matrix(m)))
        else:
            string += str(m)
    return string


@appendAll
@addBuiltins
class LoopBack(object):
    def _back(*args, **kwargs):
        pass

    def __getattribute__(self, key):
        try:
            return object.__getattribute__(self, key)
        except:
            return self._back


@appendAll
@addBuiltins
class Database(object):
    def __getattribute__(self, val):
        try:
            return object.__getattribute__(self, val)
        except:
            return self.dict[val]

    def __setattr__(self, key, val):
        if str(key).startswith("_") or str(key) in [
            "append",
            "add",
            "remove",
            "dict",
            "list",
        ]:
            object.__setattr__(self, key, val)
        else:
            self.dict[key] = val

    def __delattr__(self, val):
        try:
            del self.dict[val]
        except:
            object.__delattr__(self, val)

    def __getitem__(self, val):
        return self.list[val] if type(val) == int else self.dict[val]

    def __setitem__(self, key, val):
        self.dict[key] = val

    def __delitem__(self, val):
        del self.dict[val]

    def __repr__(self):
        return str(object.__repr__(self)).replace(
            str(str(object.__repr__(self)).split()[0]), "<Database"
        )

    def __init__(self, update=None):
        self.dict = {} if not type(update) == dict else update
        self.list = [] if not type(update) == list else update

    def append(self, val):
        self.list.append(val)

    def add(self, val):
        if len(str(val).split(":")) == 1:
            self.list.append(val)
        else:
            self.dict[str(val).split(":")[0]] = str(val).split(":")[1]

    def remove(self, val):
        self.list.remove(val)


@appendAll
@addBuiltins
class OptionsDatabase(Database):
    def __getitem__(self, val):
        return self.dict[val]

    def __repr__(self):
        return str(object.__repr__(self)).replace(
            str(str(object.__repr__(self)).split()[0]), "<OptionsDatabase"
        )

    def __add__(self, other):
        if not type(other) == OptionsDatabase:
            raise TypeError(
                f'can only concatenate OptionsDatabase (not "{type(other).__name__}") to OptionsDatabase'
            )
        newDict = {}
        for k in self.dict:
            newDict[k] = self.dict[k]
        for k in other.dict:
            newDict[k] = other.dict[k]
        return OptionsDatabase(newDict)

    def __init__(self, update=None, rules=None, allowExtraArgs=True):
        self.dict = {} if not type(update) == dict else update
        if rules:
            for i, o in enumerate(rules):
                if type(update) == tuple:
                    try:
                        if o.get("position", Empty) is Empty:
                            self.dict[o["key"]] = update[i]
                        else:
                            self.dict[o["key"]] = update[o["position"]]
                    except:
                        raise Exception(f"argument '{o['key']}' is required.")
                if not o["key"] in self.dict:
                    if o.get("required", False):
                        raise Exception(f"argument '{o['key']}' is required.")
                    self.dict[o["key"]] = o.get("default", None)
                if o.get("allowed", Empty) is not Empty:
                    if not self.dict[o["key"]] in (
                        o["allowed"] if type(o["allowed"]) == list else [o["allowed"]]
                    ):
                        raise Exception(f"value of argument '{o['key']}' is invalid.")
                if o.get("denied", Empty) is not Empty:
                    if self.dict[o["key"]] in (
                        o["denied"] if type(o["denied"]) == list else [o["denied"]]
                    ):
                        raise Exception(f"value of argument '{o['key']}' is invalid.")
                if o.get("type", Empty) is not Empty:
                    if not type(self.dict[o["key"]]) == o["type"]:
                        raise Exception(
                            f"argument '{o['key']}' must be an {o['type'].__name__} object."
                        )
                if o.get("call", Empty) is not Empty:
                    o["call"](self.dict[o["key"]])
                if o.get("update", Empty) is not Empty:
                    self.dict[o["key"]] = o["update"](self.dict[o["key"]])

        if not allowExtraArgs:
            ruleKeys = [o["key"] for o in rules]
            for k in self.dict:
                if not k in ruleKeys:
                    raise Exception(f"argument '{k}' not requested.")


@appendAll
@addBuiltins
class TextListFile(object):
    def __init__(self, filePath, newFile=None):
        self.file = open(filePath)
        self.rawdata = self.file.read()
        self.data = self.rawdata.splitlines()
        if newFile:
            self.newfile = open(newFile, "w")
            self.mode = "w"
        else:
            self.newfile = None
            self.mode = "r"

    def optimize(self):
        new = []
        for s in self.data:
            if s in new or not s:
                continue
            else:
                new.append(s)
        self.data = new

    def commit(self):
        if self.mode == "r":
            raise Exception("can't write in read mode.")
        self.newfile.write(list2str(self.data, "\n"))
        self.newfile.flush()

    def close(self):
        if self.mode == "w":
            self.newfile.close()
        self.file.close()


@appendAll
@addBuiltins
class TextDictFile(object):
    def __init__(self, filePath, newFile=None, createFile=False):
        if createFile and not _os.path.exists(filePath):
            open(filePath, "w").close()
            newFile = filePath
        self.file = open(filePath)
        self.rawdata = self.file.read()
        lines = self.rawdata.splitlines()
        if not self.checkFormat(lines):
            raise TypeError("file type not supported.")
        self.data = {}
        for l in lines:
            data = Database()
            for d, v in {
                "key": l.split(":")[0].strip(),
                "val": l.split(":")[1].strip(),
            }.items():
                try:
                    if "." in v:
                        v = float(v)
                    else:
                        v = int(v)
                except:
                    if v in ["True", "False", "None"]:
                        v = True if v == "True" else False if v == "False" else None
                    else:
                        v = str(v)
                setattr(data, d, v)
            self.data[data.key] = data.val
        if newFile:
            self.newfile = open(newFile, "w")
            self.mode = "w"
        else:
            self.newfile = None
            self.mode = "r"

    def checkFormat(self, data):
        for d in data:
            if not d:
                continue
            if d.startswith("#"):
                continue
            if not ":" in d or not len(d.split(":")) == 2:
                return False
        return True

    def commit(self):
        if self.mode == "r":
            raise Exception("can't write in read mode.")
        self.newfile.write(list2str(self.convert(), "\n"))
        self.newfile.flush()

    def convert(self, data=None):
        out = []
        if not data:
            data = self.data
        for d in data:
            out.append(str(d) + " : " + str(data[d]))
        return out

    def close(self):
        if self.mode == "w" and not self.newfile.closed:
            self.newfile.close()
        if not self.file.closeed:
            self.file.close()


def load_settings():
    global settingData
    if localSets:
        if not "light" in status:
            printWarn(
                "can't create settings file because permission denied, using default settings"
            )
        settingData = settingVals
        return settingVals
    if not _os.path.exists(settingFilePath):
        raise FileNotFoundError("settings file not found.")
    else:
        settingFile = open(settingFilePath)
        data = read_settings(settingFile.read().splitlines())
        settingFile.close()
        settingData = data
        return data


def read_settings(data):
    out = {}
    for d in data:
        extract = d.split(":")
        out[extract[0]] = extract[1]
    return out


def convert_settings(data):
    string = ""
    for s in data:
        string += s + ":" + str(data[s]) + "\n"
    return string


def setup_settings():
    global localSets
    if "light" in status:
        localSets = True
        return
    if not _os.path.exists(settingFilePath):
        try:
            settingFile = open(settingFilePath, "w")
            settingFile.write(convert_settings(settingVals))
            settingFile.flush()
            settingFile.close()
        except PermissionError:
            localSets = True
    else:
        data = load_settings()
        updated = False
        for s in settingVals:
            if not s in data:
                data[s] = settingVals[s]
                updated = True
        if updated:
            try:
                settingFile = open(settingFilePath, "w")
                settingFile.write(convert_settings(data))
                settingFile.flush()
                settingFile.close()
            except PermissionError:
                localSets = True


class Settings(object):
    def __init__(self):
        if settingData:
            self._data = settingData
        else:
            self._data = load_settings()

    def _reset(self):
        self._data = settingVals
        self._write()

    def _write(self):
        if "light" in status:
            return
        global localSets
        try:
            self._file = open(settingFilePath, "w")
            self._file.write(convert_settings(self._data))
            self._file.flush()
            self._file.close()
        except PermissionError:
            localSets = True

    def __getattr__(self, key):
        if not key.startswith("_"):
            try:
                if key == "reset":
                    self._reset()
                    printMsg("settings restored to default values")
                    return
                return self._data[key]
            except KeyError:
                printMsg("KeyError: " + "'" + key + "'", color="red")
                return
        else:
            return object.__getattribute__(self, key)

    def __setattr__(self, key, val):
        if not key.startswith("_"):
            if not key in settingVals:
                printErr("option is invalid")
                return
            if key in settingChoices and not val in settingChoices[key]:
                printErr("value is invalid")
                return
            self._data[key] = val
            self._write()
        else:
            object.__setattr__(self, key, val)


setup_settings()
settings = appendAll(Settings(), "settings")


class ProtectedDict(dict):
    def __init__(self, *args, **kwargs):
        dict.__init__(self, *args, **kwargs)
        if settings.saveDatabase == "on" and not localSets:
            if not _os.path.exists(databaseFilePath):
                self.dataFile = TextDictFile(databaseFilePath, createFile=True)
                self.dataFile.file.close()
            else:
                self.dataFile = TextDictFile(databaseFilePath, databaseFilePath)
                self.dataFile.commit()
                self.dataFile.file.close()
                for d in self.dataFile.data:
                    dict.__setitem__(self, d, self.dataFile.data[d])
        else:
            self.dataFile = None

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def __setitem__(self, key, val):
        raise TypeError("can't change ProtectedDict contents")

    def __getitem__(self, key):
        raise TypeError("can't see ProtectedDict contents")

    def __delitem__(self, key):
        raise TypeError("can't change ProtectedDict contents")


@appendAll
@addBuiltins
class SecureDatabase(object):
    def __init__(self, id, data={}, replace=False, clearOnDelete=False):
        self.id = id
        if not hasID(id) or replace:
            setID(id, data, False)
        self.data = getID(id)
        self.dataType = type(self.data)
        self.CON = clearOnDelete

    def __repr__(self):
        return self.data.__repr__()

    def __str__(self):
        return self.data.__str__()

    def __add__(self, other):
        return self.data.__add__(other)

    def __format__(self):
        return self.data.__format__()

    def __len__(self):
        return self.data.__len__()

    def __eq__(self, other):
        return self.data.__eq__(other)

    def __ge__(self, other):
        return self.data.__ge__(other)

    def __gt__(self, other):
        return self.data.__gt__(other)

    def __hash__(self):
        return self.data.__hash__()

    def __iter__(self):
        return self.data.__iter__()

    def __ne__(self, other):
        return self.data.__ne__(other)

    def __truediv__(self, other):
        return self.data.__truediv__(other)

    def __rtruediv__(self, other):
        return self.data.__rtruediv__(other)

    def __div__(self, other):
        return self.data.__div__(other)

    def __sub__(self, other):
        return self.data.__sub__(other)

    def __mul__(self, other):
        return self.data.__mul__(other)

    def __rmul__(self, other):
        return self.data.__rmul__(other)

    def __rsub__(self, other):
        return self.data.__rsub__(other)

    def __le__(self, other):
        return self.data.__le__(other)

    def __lt__(self, other):
        return self.data.__lt__(other)

    def __del__(self):
        if self.CON:
            delID(self.id)

    def __setitem__(self, key, val):
        self.data.__setitem__(key, val)
        self.update()

    def __getitem__(self, key):
        return self.data.__getitem__(key)

    def __delitem__(self, key):
        self.data.__delitem__(key)
        self.update()

    def __setattr__(self, key, val):
        object.__setattr__(self, key, val)
        if key == "data":
            self.dataType = type(self.data)
            self.update()

    def update(self):
        setID(self.id, self.data, False)


@appendAll
def getID(id, default=None):
    global database
    try:
        return dict.__getitem__(database, id)
    except KeyError:
        return default


@appendAll
def hasID(id):
    global database
    return id in database


@appendAll
def setID(id, data, exceptOnDup=True):
    global database
    if hasID(id):
        if exceptOnDup:
            raise TypeError("can't set duplicate id.")
    dict.__setitem__(database, id, data)
    if database.dataFile is not None:
        database.dataFile.newfile.write(
            list2str(database.dataFile.convert({id: data})) + "\n"
        )
        database.dataFile.newfile.flush()


@appendAll
def delID(id):
    global database
    dict.__delitem__(database, id)


database = ProtectedDict()


class TimerThread(_threading.Thread):
    def __init__(self, id, time, call, repeat=False):
        _threading.Thread.__init__(self)
        self.id = id
        self.time = time
        self.call = call
        self.repeat = repeat

    def run(self):
        run = True
        while run:
            if getID(self.id, "stopped") == "stopped":
                break
            _time.sleep(self.time)
            if getID(self.id, "stopped") == "stopped":
                break
            if callable(self.call):
                self.call()
            if not self.repeat:
                run = False
        delID(self.id)


@appendAll
@addBuiltins
class Timer(object):
    def __init__(self, time, call, repeat=False, type="background"):
        self.type = type
        if str(time)[-1] in ["s", "m", "h"]:
            unit = str(time)[-1]
            time = float(str(time)[:-1])
            if unit in ["m", "h"]:
                time = time * 60
            if unit in ["h"]:
                time = time * 60
        time = float(time)
        self.id = int(getRandomString(10, ["numbers"]))
        setID(self.id, "started", False)
        thread = TimerThread(self.id, time, call, repeat)
        if type == "background":
            thread.daemon = True
            thread.start()
        elif type == "foreground":
            thread.run()
        else:
            printErr("type is invalid")

    def __repr__(self):
        return f'<{self.__class__.__name__} {getID(self.id, "stopped")} ID={str(self.id) if hasID(self.id) else str(None)}>'

    def __del__(self):
        setID(self.id, "stopped", False)


@appendAll
@addBuiltins
class Call(object):
    def __init__(self, *args, **keywds):
        self.call = args[0]
        self.args = args[1:]
        self.keywds = keywds

    def __call__(self, *argsExtra):
        return self.call(*self.args + argsExtra, **self.keywds)

    def __repr__(self):
        return (
            "<Call object call="
            + str(self.call)
            + " args="
            + str(self.args)
            + " keywds="
            + str(self.keywds)
            + ">"
        )


@appendAll
@addBuiltins
class Widget(object):
    def __init__(self, progressNeeded=False):
        self.reprMsg = "<$name Widget>".replace("$name", str(self.__class__.__name__))
        self.progress = None
        self._finished = False
        self.progressNeeded = progressNeeded

    def _set_progress(self, progress):
        if not isinstance(progress, Progress):
            raise TypeError(str(progress) + " must be instance of " + str(Progress))
        self.progress = progress

    def _finish(self):
        self._finished = True

    def __repr__(self):
        return self.reprMsg

    def __call__(self):
        if self.progressNeeded and self.progress is None:
            raise Exception("progress instance needed.")


@appendAll
@addBuiltins
class TimeWidget(Widget):
    def __init__(self, milisec=False, min=True, hour=True):
        Widget.__init__(self)
        self.milisec = milisec
        self.min = min
        self.hour = hour
        self._startTime = _time.time()
        self.startTime = int(self._startTime)

    def calc_time(self):
        _now = _time.time()
        now = int(_now)
        string = ""
        if self.milisec:
            milisec = str(_now - self._startTime).split(".")[1][:3]
        sec = now - self.startTime
        min = 0
        hour = 0
        if sec >= 60 and self.min:
            for m in range(sec // 60):
                sec -= 60
                min += 1
        if min >= 60 and self.hour:
            for m in range(min // 60):
                min -= 60
                hour += 1
        if len(str(hour)) <= 1:
            hour = "0" + str(hour)
        if len(str(min)) <= 1:
            min = "0" + str(min)
        if len(str(sec)) <= 1:
            sec = "0" + str(sec)
        if self.hour:
            string += str(hour) + ":"
        if self.min:
            string += str(min) + ":"
        if self.milisec:
            sec = str(sec) + "." + milisec
        string += str(sec)
        return string

    def __call__(self):
        Widget.__call__(self)
        return self.calc_time()


@appendAll
@addBuiltins
class BarWidget(Widget):
    def __init__(self, fill="█", empty="░", fillPerPercent=5, color=None):
        Widget.__init__(self, True)
        self.fill = fill
        self.empty = empty
        self.fpp = fillPerPercent
        self.color = color

    def __call__(self):
        Widget.__call__(self)
        return self.createBar()

    def createBar(self):
        perc = int(self.progress.calc_perc().split(".")[0])
        bar = ""
        filled = 0
        if perc >= self.fpp:
            for c in range(perc // self.fpp):
                bar += self.fill
                filled += 1
        for f in range(100 // self.fpp - filled):
            bar += self.empty
        if self.color and verifyColor(self.color, False):
            bar = "-" + self.color + bar + "*end"

        return bar


@appendAll
@addBuiltins
class TaskWidget(Widget):
    def __init__(self, tasks={}):
        Widget.__init__(self, True)
        self.tasks = tasks
        self.percTasks = {}
        self.eventTasks = {}
        self.firstRun = True
        self.checkTasks()

    def checkTasks(self):
        for t in self.tasks:
            if t == "perc":
                self.percTasks = self.tasks[t]
            elif t == "event":
                self.eventTasks = self.tasks[t]

    def __call__(self):
        Widget.__call__(self)
        return calc_task()

    def calc_task(self):
        if self.eventTasks:
            if "onFirstShow" in self.eventTasks and self.firstRun:
                self.firstRun = False
                return self.eventTasks["onFirstShow"]
            if "onFinish" in self.eventTasks and self._finished:
                return self.eventTasks["onFinish"]
        if self.percTasks:
            perc = int(self.progress.calc_true_perc())
            for p in self.percTasks:
                if perc <= p:
                    return self.percTasks[p]
        return ""


@appendAll
@addBuiltins
class CallWidget(Widget):
    def __init__(self, call, progressNeeded=False):
        Widget.__init__(self, progressNeeded)
        self.call = call

    def __call__(self):
        Widget.__call__(self)
        if self.progressNeeded:
            return self.call(self.progress)
        else:
            return self.call()


@appendAll
@addBuiltins
class ValueWidget(Widget):
    def __init__(self, value):
        Widget.__init__(self)
        self.value = value

    def __call__(self):
        Widget.__call__(self)
        return self.value


@appendAll
@addBuiltins
class LoadingWidget(Widget):
    def __init__(self, type="default"):
        Widget.__init__(self)
        self.type = type
        self.index = 0
        self.msg = None
        self.loadingType = None
        self.handleType()

    def handleType(self):
        typeData = self.getTypes()[self.type]
        self.msg = typeData["data"]
        self.loadingType = type(typeData["data"])
        if self.loadingType == str:
            self.msg = ProtString(self.msg)

    def createMsg(self):
        if self._finished:
            return "done"
        if self.loadingType == list:
            msg = self.msg[self.index]
            if self.index + 1 == len(self.msg):
                self.index = 0
            else:
                self.index += 1
            return msg
        else:
            msg = self.msg
            end = self.msg[-1]
            del self.msg[-1]
            self.msg = self.msg.query
            self.msg = ProtString(end + str(self.msg))
            return msg

    def __call__(self):
        Widget.__call__(self)
        return self.createMsg()

    def getTypes(self):
        return {
            "default": {"data": ["|", "-"]},
            "bar": {"data": "█████               "},
            "smallbar": {"data": "███         "},
            "verysmallbar": {"data": "██      "},
        }


@appendAll
@addBuiltins
class LockedDict(dict):
    def __delitem__(self, val):
        raise TypeError("dict is locked.")

    def __setitem__(self, key, val):
        raise TypeError("dict is locked.")


@appendAll
@addBuiltins
class Progress(object):
    _deafultForm = "($VAL/$MAX) $PERC% $MSG"

    def __init__(
        self,
        val=0,
        minVal=0,
        maxVal=100,
        msg="completed",
        msgForm=None,
        replaces=[],
        color=None,
        inline=False,
    ):
        self._finished = False
        self.val = val
        self.min = minVal
        self.max = maxVal
        self.msg = msg
        self.inline = (
            inline
            if _sys.stdout == _sys.__stdout__ and (not _os.name == "nt" or _c)
            else False
        )
        self.color = color
        if not msgForm:
            self.msgForm = self.get_default_form()
        else:
            self.msgForm = msgForm
        if replaces:
            for r in replaces:
                if not isinstance(r[1], Widget):
                    raise TypeError(str(r[1]) + " must be instance of Widget")
                r[1]._set_progress(self)
            self.extraReplaces = replaces
        else:
            self.extraReplaces = []
        self.show()

    def show(self):
        replaces = self.getDefaultReplaces()
        msg = self.do_replace(replaces)
        if self.color and verifyColor(self.color, False):
            msg = "-" + self.color + msg + "*end"
        if self.inline:
            self.printInline(msg)
        else:
            printMsg(msg)

    def getDefaultReplaces(self):
        return [
            ["$VAL", self.val],
            ["$MIN", self.min],
            ["$MAX", self.max],
            ["$PERC", self.calc_perc()],
            ["$TRUE_PERC", self.calc_true_perc()],
            ["$MSG", self.msg],
        ]

    def clear(self):
        printMsg("\r\x1b[K", end="", prefix=False)

    def printInline(self, msg):
        self.clear()
        printMsg(msg, end="")

    def write(self, msg=""):
        if self.inline:
            printMsg("\n" + msg)
        else:
            printMsg(msg)

    def newline(self):
        if self.inline:
            printMsg("", prefix=False)

    def finish(self):
        for r in self.extraReplaces:
            r[1]._finish()
        self._finished = True
        self.newline()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish()

    def get_default_form(self):
        return self._deafultForm

    def calc_perc(self):
        perc = str(100 / self.max * self.val).split(".")
        perc[1] = perc[1][:3]
        return perc[0] + "." + perc[1]

    def calc_true_perc(self):
        perc = str(100 / self.max * self.val).split(".")[0]
        return perc

    def do_replace(self, rl):
        cf = self.msgForm if not hasattr(self, "tempMsg") else self.tempMsg
        for r in rl:
            cf = cf.replace(r[0], str(r[1]))
        for r in self.extraReplaces:
            cf = cf.replace(r[0], str(r[1]()))
        if "$" in cf and not hasattr(self, "tempMsg"):
            self.tempMsg = cf
            self.do_replace(rl)
        else:
            try:
                del self.tempMsg
            except:
                pass
            return cf

    def update(self, val):
        self.val = max(self.min, min(self.max, val))
        self.show()

    def next(self, val=1):
        self.val = max(self.min, min(self.max, self.val + val))
        self.show()


@appendAll
@addBuiltins
class ProgressBar(Progress, BarWidget):
    def __init__(
        self,
        val=0,
        minVal=0,
        maxVal=100,
        msg="completed",
        msgForm=None,
        replaces=[],
        color=None,
        inline=False,
        fill="█",
        empty="░",
        fillPerPercent=5,
    ):
        BarWidget.__init__(self, fill=fill, empty=empty, fillPerPercent=fillPerPercent)
        Progress.__init__(
            self,
            val=val,
            minVal=minVal,
            maxVal=maxVal,
            msg=msg,
            msgForm=msgForm,
            replaces=replaces,
            color=color,
            inline=inline,
        )
        self.progress = self

    def __repr__(self):
        return object.__repr__(self)

    def getDefaultReplaces(self):
        Progress.getDefaultReplaces(self) + [["$BAR", self()]]

    def finish(self):
        self._finish()
        Progress.finish(self)


@appendAll
@addBuiltins
class VersionString(str):
    def __init__(self, *args, **kwargs):
        str.__init__(self)
        try:
            ver = self.split(".")
            try:
                self.major = int(ver[0])
            except:
                self.major = None
            try:
                self.minor = int(ver[1])
            except:
                self.minor = None
            try:
                self.micro = int(ver[2])
            except:
                self.micro = None
        except:
            pass

    def upgrade(self, target="default", maxMinor=9, maxMicro=9):
        if target == "default":
            if self.micro is not None:
                target = "micro"
            elif self.minor is not None:
                target = "minor"
            elif self.major is not None:
                target = "major"
        if self.micro is not None and self.micro >= maxMicro:
            minor = True
        else:
            minor = False
        if self.minor is not None and self.minor >= maxMinor:
            major = True
        else:
            major = False
        if False:
            print(f"target: {str(target)}")
            print(f"self.micro: {str(self.micro)}")
            print(f"maxMicro: {str(maxMicro)}")
            print(f"self.minor: {str(self.minor)}")
            print(f"maxMinor: {str(maxMinor)}")
            print(f"minor: {str(minor)}")
            print(f"self.major: {str(self.major)}")
            print(f"major: {str(major)}")
        if self.micro is not None and target == "micro":
            self.micro += 1
        if self.minor is not None and (target == "minor" or minor) and not major:
            if self.micro is not None:
                self.micro = 0
            self.minor += 1
        if self.major is not None and (target == "major" or (major and minor)):
            if self.micro is not None:
                self.micro = 0
            if self.minor is not None:
                self.minor = 0
            self.major += 1
        return self.compile()

    def compile(self):
        ver = []
        if self.major is not None:
            ver.append(str(self.major))
        if self.minor is not None:
            ver.append(str(self.minor))
        if self.micro is not None:
            ver.append(str(self.micro))
        return ".".join(ver)


@appendAll
@addBuiltins
class ProtString(str):
    def compile(self):
        try:
            if "." in self:
                out = float(self)
            else:
                out = int(self)
        except:
            if self in ["True", "False", "None"]:
                out = True if self == "True" else False if self == "False" else None
            else:
                out = str(self)
        return out

    @property
    def type(self):
        return self.split(".")[-1].lower()

    @property
    def has_type(self):
        return len(self.split(".")) > 1

    def extract(self):
        splittedList = self.split(",")
        splittedDict = {}
        splittedListNew = []
        for i in splittedList:
            if len(i.split(":")) > 1:
                splittedDict[i.split(":")[0]] = i.split(":")[1]
        for i in splittedList:
            if len(i.split(":")) > 1:
                for s in i.split(":"):
                    splittedListNew.append(s)
            else:
                splittedListNew.append(i)
        if len(splittedListNew) == 0 and len(splittedDict) == 0:
            raise ValueError("this string is not encoded.")
        else:
            data = Database()
            for i in splittedListNew:
                data.append(i)
            for i in splittedDict:
                data[i] = splittedDict[i]
            return data

    def __setitem__(self, index, val):
        stringList = []
        for string in self:
            stringList.append(string)
        stringList[index] = str(val)
        compiledString = ""
        for string in stringList:
            compiledString += string
        self.query = self.__class__(compiledString)

    def __delitem__(self, key):
        stringList = []
        for string in self:
            stringList.append(string)
        del stringList[key]
        compiledString = ""
        for string in stringList:
            compiledString += string
        self.query = self.__class__(compiledString)

    def __div__(self, other):
        out = []
        try:
            if len(self) > other:
                splitDelay = len(self) // other
                tStr = str(self)
                for i in range(splitDelay):
                    out.append(tStr[:other])
                    tStr = tStr[other:]
                if not tStr == "":
                    out.append(tStr)
            else:
                out = [self]
        except:
            out = []
        return out
