#!/usr/local/bin/python3.7
import import_getenv

def main():
    import sys
    import os
    print('Python %s on %s' % (sys.version, sys.platform))
    PYTHON_COMMON_PY = os.getenv('PYTHON_COMMON_PY', '')
    print(PYTHON_COMMON_PY)
