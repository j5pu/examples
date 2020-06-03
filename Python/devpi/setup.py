import setuptools
import os
import sys

__package__ = os.path.basename(os.getcwd())
__version__ = {}

with open("version.py") as fp:
    exec(fp.read(), version)

def main():
    setuptools.setup(
        name = package_name,
        description = 'A insignificant project for the sake of documentation',
        url = 'http://1a1.host',
        version = version['__version__'],
        author = 'Carlo Coehlo',
        author_email = 'cc1@openmai.cc',
        # packages=setuptools.find_packages(),
        # packages = ["example_devpi"],
        py_modules = ["example_devpi","version"],
        python_requires = '>=3.7',
        classifiers = [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.7",
            "Operating System :: POSIX :: Linux",
        ],
        include_package_data=True,
        zip_safe = False,
    )

if __name__ == '__main__':
    main()
    # print(setuptools.find_packages())
    # print(setuptools.findall())
