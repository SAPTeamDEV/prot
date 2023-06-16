import builtins as _builtins

from . import *

maps = {}
depends = []


class Map(object):
    name = "Map"

    @classmethod
    def getPreviewTextureName(cls):
        """
        Return the name of the preview texture for this map.
        """
        return None

    @classmethod
    def onPreload(cls):
        """
        Called when the map is being preloaded;
        it should load any media it requires to
        class attributes on itself.
        """
        return None


def registerMap(map):
    if not map.name in maps:
        maps[map.name] = map
    else:
        raise Exception(repr(map.name) + "already exists.")


def _import(*args, **kwargs):
    depends.append(args[0])
    if _import.redirect:
        return _builtins.__import(*args, **kwargs)


def record(redirect=False):
    if redirect:
        _import.redirect = True
    else:
        _import.redirect = False
    _builtins.__import = _builtins.__import__
    _builtins.__import__ = _import


def end():
    _builtins.__import__ = _builtins.__import
    del _builtins.__import
    del _import.redirect


def clear():
    global maps
    global depends
    maps = {}
    depends = []


def getMedia(path=".", divide=False, silent=False):
    tree = bs.makeTree(path)
    data = {}
    for name, obj in maps.items():
        medias = []
        preloads = []
        if obj.getPreviewTextureName() is not None:
            medias += bs.getFiles(obj.getPreviewTextureName(), path, ["ktx", "dds"])
        if obj.onPreload() is not None:
            for key, value in obj.onPreload().items():
                if type(value) == str:
                    preloads.append(value)
                elif type(value) in [list, tuple]:
                    preloads += list(value)
        for preload in preloads:
            if preload.endswith(".texture"):
                medias += bs.getFiles(preload.split(".")[0], path, ["ktx", "dds"])
            else:
                medias.append(preload)
        for depend in depends:
            medias += bs.getFiles(depend, path, ["py", "pyc"])
        data[name] = [ProtString(media) for media in medias]

    if data:
        bs.processMedia(data, path, divide, silent)
