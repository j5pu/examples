# [PyPi](https://python-packaging.readthedocs.io/en/latest/minimal.html)
## Directories
```shell script
imports_getenv/
    imports_getenv/
        __init__.py
    setup.py
```
### Instalar
```shell script
pip install .
```
### Instalar symlink
```shell script
pip install -e .
```
## Publish Package
### Register package
```shell script
python setup.py register
```
### View info
```shell script
open http://pypi.python.org/pypi/imports_getenv/0.1
```
### Create source distribution
```shell script
python setup.py sdist
```
### Upload distribution
```shell script
python setup.py sdist upload
```
### Create & Upload Distribution in one command
```shell script
python setup.py register sdist upload
```
### All setup.py commands
```shell script
python setup.py --help-commands
```
## Install Package
```shell script
pip install imports_getenv
```

## Adding Additional Files
Debajo del módulo:
```shell script
imports_getenv/
    imports_getenv/
        __init__.py
        imports.py
        getenv.py
    setup.py
```
En __init__.py:
```python
from .imports import *
from .getenv import *
```
### View info
```shell script
open http://pypi.python.org/pypi/imports_getenv/0.1
```
### Create source distribution
```shell script
python setup.py sdist
```
### Upload distribution
```shell script
python setup.py sdist upload
```
## Dependencias
En módulo.py (imports.py):
```python
import os

```
Para comprobar:
```shell script
python setup.py develop
```
## Better Metadata
En módulo.py (imports.py):
```python
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      packages=['funniest'],
      include_package_data=True,
```
Para comprobar:
```shell script
python setup.py develop
```
## MANIFEST.in
This file is necessary to tell setuptools to include the README.rst file when generating source distributions. Otherwise, only Python files will be included
```in
include README.rst
```
En setup.py:
```python
def readme():
    with open('README.rst') as f:
        return f.read()
```
When the repo is hosted on GitHub or BitBucket, the README.rst file will also automatically be picked up and used as a ‘homepage’ for the project.
## Test
En tests/test_import.py:
```python
from unittest import TestCase

import funniest

class TestJoke(TestCase):
    def test_is_string(self):
        s = funniest.joke()
        self.assertTrue(isinstance(s, basestring))
```
The best way to get these tests going (particularly if you’re not sure what to use) is Nose. With those files added, it’s just a matter of running this from the root of the repository:
```shell script
pip install nose
nosetests
```
To integrate this with our setup.py:
```python
setup(
    ...
    test_suite='nose.collector',
    tests_require=['nose'],
)
```
Run test:
```shell script
python setup.py test
```
## Command Line Scripts
Many Python packages include command line tools. This is useful for distributing support tools which are associated with a library, or just taking advantage of the setuptools / PyPI infrastructure to distribute a command line tool that happens to use Python.

Añadimos imports_getenv CLT
2 métodos:
    - the scripts keyword argument,
    - and the console_scripts entry point

### The scripts Keyword Argument (any script: bash, python..)
The first approach is to write your script in a separate file, such as you might write a shell script.:
```
    bin/
        imports_getenv_start
```
When we install the package, setuptools will copy the script to our PATH and make it available for general use
```python
imports_getenv
```
### The console_scripts Entry Point
The second approach is called an ‘entry point’. Setuptools allows modules to register entrypoints which other packages can hook into to provide certain functionality. It also provides a few itself, including the console_scripts entry point.
***This allows Python functions (not scripts!) to be directly registered as command-line accessible tools.***
Se añade entry_point_command_line.py, que es un módulo solo para servir el CLT, y se prueba:
```python
python
```
Se prueba con test case:
```python
from unittest import TestCase
from funniest.command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()
```
## Adding Non-Code Files
The mechanism that provides this is the MANIFEST.in file. This is relatively quite simple: MANIFEST.in is really just a list of relative file paths specifying files or globs to include.:
```shell script
include README.rst
include imports_getenv/data.json
```
# [Packaging](https://packaging.python.org/overview/)
**If your code consists of multiple Python files, it’s usually organized into a directory structure**. ***Any directory containing Python files can comprise an import package***.
## Generating distribution archives
***The next step is to generate distribution packages for the package***:
```shell script
python3 -m pip install --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
```
## Uploading the distribution archives
***you can use twine to upload the distribution packages. You’ll need to install Twine***:
```shell script
python3 -m pip install --upgrade twine
```
Subir a test:
```shell script
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Con usuario PyPi ($HOME/pypirc para usuario y contraseña)
```shell script
twine upload dist/*
```
## Install
***you can use twine to upload the distribution packages. You’ll need to install Twine***:
```shell script
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-your-username
```
### Install specific versions
```shell script
pip install requests==2.18.4
pip install requests>=2.0.0,<3.0.0
# pre-release
pip install --pre requests
```

