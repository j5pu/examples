# from __future__ import absolute_import
# from .version import __version__
import sys

from version import main

# version = __version__
def get_version():
    version = main()
    print(version)
    return version

get_version()