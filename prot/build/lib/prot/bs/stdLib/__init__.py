import sys
import os

from . import bs

if not sys.version_info[0] == 2:
    raise ImportError('this package made for python 2.')

sys.path.append(os.path.split(__file__)[0])

del sys
del os