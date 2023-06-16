import sys

import prot

from . import *
from . import __version__ as version

exit = False
if "light" in status:
    printErr("command line interface not available in light version")
    exit = True

if __name__ == "__main__" and not exit:
    for a in sys.argv[1:]:
        if a in ["version", "v"]:
            printMsg(version)
            break
        if a in ["tools", "t"]:
            ea = sys.argv[2]
            if ea in ["test", "t"]:
                try:
                    c = int(sys.argv[3])
                except:
                    c = 1000
                testSpeed(c)
            elif ea in ["wait", "w"]:
                try:
                    c = float(sys.argv[3])
                except:
                    try:
                        c = str(sys.argv[3])
                    except:
                        c = 1.0
                Timer(c, None, False, "foreground")
            else:
                printErr("argument is invalid.")
            break
        elif a in ["set", "s"]:
            if len(sys.argv) == 2:
                for s in settings._data:
                    printMsg(s + " : " + settings._data[s])
            elif len(sys.argv) == 3:
                res = getattr(settings, sys.argv[2])
                if res:
                    printMsg(sys.argv[2] + " : " + res)
            elif len(sys.argv) == 4:
                setattr(settings, sys.argv[2], sys.argv[3])
                try:
                    if getattr(settings, sys.argv[2]) == sys.argv[3]:
                        printMsg(sys.argv[2] + " : " + sys.argv[3])
                except:
                    pass
            else:
                printErr("argument is invalid.")
            break
        elif a in ["run", "r"]:
            func = sys.argv[2]
            try:
                args = sys.argv[3:]
            except:
                args = []
            cargs = []
            for a in args:
                try:
                    integer = int(a)
                except:
                    integer = None
                if a.startswith("!"):
                    try:
                        data = ProtString(a[1:]).extract()
                        if len(data.dict) > 0:
                            narg = data.dict
                        elif len(data.list) > 0:
                            narg = data.list
                        else:
                            narg = []
                        if narg:
                            if type(narg) == list and len(narg) == 1 and not narg[0]:
                                narg = []
                        else:
                            narg = []
                    except:
                        try:
                            integer = int(a[1:])
                        except:
                            integer = None
                        if integer:
                            narg = integer
                        else:
                            narg = str(a[1:])
                elif integer:
                    narg = integer
                elif a in ["True", "False", "None"]:
                    narg = True if a == "True" else False if a == "False" else None
                else:
                    narg = str(a)
                cargs.append(narg)
            res = getattr(prot, func)(*cargs)
            if res:
                printMsg(res)
        elif a in ["update", "u"]:
            printMsg("current version is " + version)
            if "unofficial" in status:
                printErr("can't update an unofficial product")
                break
            printMsg("checking for updates...")
            try:
                from prot.pip.extra import packageReleases

                ver = int(list2str(version.split(".")))
                vers = packageReleases("prot")
                updateAvail = False
                for v in vers:
                    cver = int(list2str(v.split(".")))
                    if cver > ver:
                        updateAvail = True
                        insver = v
                        break
                if updateAvail:
                    printMsg("new version found, Installing prot v" + insver)
                    try:
                        runAsMain("pip -q install --upgrade prot==" + insver)
                    except:
                        pass
                else:
                    printMsg("latest version already installed")
            except:
                printErr("update failed.")
        else:
            printErr("argument is invalid.")
        break
