import json
from base64 import b64encode

from . import *


def bpp2cbpp(source):
    with open(source) as file:
        codesList = [row for row in file]
    codedStr = None
    stdStr = ""
    for c in codesList:
        if str(c).startswith("#  # #"):
            codedStr = c
        else:
            stdStr = stdStr + c

    if codedStr is not None:
        bCodedStr = b64encode(codedStr)
    else:
        bCodedStr = None
    if stdStr:
        bStdStr = b64encode(stdStr)
    else:
        bStdStr = None
    if bCodedStr is not None and bStdStr is not None:
        fCode = bCodedStr + "\n" + bStdStr
    else:
        fCode = bStdStr
    with open(source.split(".")[0] + ".cbpp", "wb") as nf:
        nf.write(fCode)
        nf.flush()


def py2jbpp(source):
    exec(open(source).read())
    with open(source.split(".")[0] + ".jbpp", "w") as nf:
        nf.write(json.dumps(dict))
        nf.flush()
