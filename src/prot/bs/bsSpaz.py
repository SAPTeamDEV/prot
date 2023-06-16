import os
import shutil

from . import *

appearances = {}


class Appearance(Database):
    def __init__(self, name):
        Database.__init__(self)
        if not name in appearances:
            appearances[name] = self
        else:
            raise Exception(repr(name) + "already exists.")


def clear():
    global appearances
    appearances = {}


def getOutput(file):
    string = ""
    for a in appearances:
        string += (
            "addCharacter(" + repr(a) + ", cfg=" + str(appearances[a].dict) + ")\n"
        )

    with open(file, "w") as f:
        f.write(string)
        f.flush()


def getMedia(path=".", divide=False, silent=False):
    tree = bs.makeTree(path)
    data = {}
    for name, obj in appearances.items():
        medias = []
        for key, value in obj.dict.items():
            if type(value) == str:
                values = [value]
            elif type(value) in [list, tuple]:
                values = list(value)
            else:
                continue
            for fileName in values:
                medias += bs.getFiles(
                    fileName, path, ["ogg", "ktx", "dds", "bob", "cob"]
                )
        data[name] = [ProtString(media) for media in medias]

    if data:
        bs.processMedia(data, path, divide, silent)
