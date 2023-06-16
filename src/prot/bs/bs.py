import hashlib
import os
import shutil
from base64 import b64encode
from functools import partial

from . import *

treeCache = {}


def getModel(file):
    return file + ".bob"


def getCollideModel(file):
    return file + ".cob"


def getTexture(file):
    return file + ".texture"


def getSound(file):
    return file + ".ogg"


class Material(LoopBack):
    pass


class Factory(object):
    def __setattr__(self, key, value):
        if key in ["dict", "getcontents"] or key.startswith("_"):
            object.__setattr__(self, key, value)
        if not hasattr(self, "dict"):
            self.dict = {}
        self.dict[key] = value

    def __getattribute__(self, key):
        if key in ["dict", "getcontents"] or key.startswith("_"):
            return object.__getattribute__(self, key, value)
        if not hasattr(self, "dict"):
            self.dict = {}
        return self.dict[key]

    def getcontents(self, path="."):
        files = []
        data = {self.__class__.__name__: files}
        for key, value in self.dict.items():
            if type(value) == str:
                values = [value]
            elif type(value) in [list, tuple]:
                values = list(value)
            else:
                continue
            for fileName in values:
                if fileName.endswith(".texture"):
                    files += bs.getFiles(fileName.split(".")[0], path, ["ktx", "dds"])
                else:
                    files.append(fileName)
        return data


def md5sum(filename):
    with open(filename, mode="rb") as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b""):
            d.update(buf)
    return d.hexdigest()


def genPayloadInfo():
    files = []
    for root, subdirs, files_in_dir in os.walk(".", topdown=True, followlinks=False):
        for file in files_in_dir:
            if file.startswith(".") or file == "payload_info":
                continue
            files.append(os.path.join(root, file))

    payloadStr = "{}\n1\n".format(len(files))
    for file in files:
        payloadStr += "{} {}\n".format(file.strip("./"), md5sum(file))

    with open("payload_info", "w") as f:
        f.write(payloadStr)
        f.close()


def getFiles(file, path=".", formats=["ogg", "ktx", "dds", "bob", "cob", "py", "pyc"]):
    tree = makeTree(path)
    files = []
    for format in formats:
        if file + "." + format in tree:
            files.append(file + "." + format)
    return files


def makeTree(source=".", ignoreCache=False):
    if source in treeCache and not ignoreCache:
        return treeCache[source]
    tree = {}
    for p in os.listdir(source):
        if os.path.isdir(os.path.join(source, p)):
            for name, path in makeTree(os.path.join(source, p)).items():
                tree[name] = path
        else:
            tree[p] = os.path.join(source, p)
    if not ignoreCache:
        treeCache[source] = tree
    return tree


def encodeFile(source):
    ff = open("coded-" + source, "wb")
    ff.write(
        "import base64;exec(base64.b64decode("
        + repr(b64encode(open(source).read()))
        + "))"
    )
    ff.flush()


def processMedia(data, path=".", divide=False, silent=False):
    tree = makeTree(path)
    media = os.path.join(path, "media")
    if not os.path.isdir(media):
        os.mkdir(media)
    for name, files in data.items():
        if divide:
            media = os.path.join(media, name)
            if not os.path.isdir(media):
                os.mkdir(media)

        audios = os.path.join(media, "audios")
        tex = os.path.join(media, "textures")
        texAndroid = os.path.join(tex, "android")
        texOther = os.path.join(tex, "other")
        models = os.path.join(media, "models")
        scripts = os.path.join(media, "scripts")

        if not os.path.isdir(audios):
            os.mkdir(audios)
        if not os.path.isdir(tex):
            os.mkdir(tex)
        if not os.path.isdir(texAndroid):
            os.mkdir(texAndroid)
        if not os.path.isdir(texOther):
            os.mkdir(texOther)
        if not os.path.isdir(models):
            os.mkdir(models)
        if not os.path.isdir(scripts):
            os.mkdir(scripts)

        audioFormats = ["ogg"]
        texFormats = ["dds", "ktx"]
        modelFormats = ["bob", "cob"]
        scriptFormats = ["py", "pyc"]

        for file in files:
            if file in tree:
                if file.type in audioFormats:
                    if not silent:
                        print(file + " -> " + audios)
                    shutil.copy(tree[file], audios)
                elif file.type in texFormats:
                    if file.type == "ktx":
                        if not silent:
                            print(file + " -> " + texAndroid)
                        shutil.copy(tree[file], texAndroid)
                    else:
                        if not silent:
                            print(file + " -> " + texOther)
                        shutil.copy(tree[file], texOther)
                elif file.type in modelFormats:
                    if not silent:
                        print(file + " -> " + models)
                    shutil.copy(tree[file], models)
                elif file.type in scriptFormats:
                    if not silent:
                        print(file + " -> " + scripts)
                    shutil.copy(tree[file], scripts)
                else:
                    printWarn("type of file " + file + " is not supported")
            else:
                printWarn("file " + file + " not found")
