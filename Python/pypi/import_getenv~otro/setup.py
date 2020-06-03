import setuptools

def readme():
    # with open("README.md", "r") as fh:
    #     long_description = fh.read()
    with open("README.rst") as f:
        return f.read()

version = {}
with open("import_getenv/version.py") as fp:
    exec(fp.read(), version)

setuptools.setup(
    name = "import_getenv",
    version = version['__version__'],
    license = "MIT",
    author = "Carlo Coehlo",
    author_email = "cc1@openmai.cc",
    description = "Set of imports and os.getenv to be shared accross projects.",
    long_description = readme(),
    # install_requires = ["os"],
    # install_requires = ['django-pipeline==1.1.22', 'south>=0.7']
    packages = setuptools.find_packages(),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: POSIX :: Linux",
    ],
    test_suite = "nose.collector",
    tests_require = ["nose"],
    include_package_data = True,
    scripts = ["bin/import_getenv_start"],
    entry_points = {
        "console_scripts": ["import_getenv=import_getenv.entry_point_command_line:main"],
    },
    python_requires = '>=3.7',
    zip_safe = False
)
