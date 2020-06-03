# [Uploading, testing and pushing](https://devpi.net/docs/devpi/devpi/stable/+d/userman/devpi_packages.html)
***/root/pypi is a special cache to https://pypi.org***
## Installing
```shell script
devpi login fp --password=1Zaragoza$.
devpi index -l
devpi use $DEVPI
devpi use -l

devpi use fp/dev
devpi index -c fp/prod bases=root/pypi volatile=False
# ó
devpi index -c fp/prod
devpi index fp/dev bases+=root/pypi

devpi install lazy
```
## Uploading Release File
The upload command effectively calls python setup.py register and python setup.py sdist upload using a wrapper script that makes sure we are doing these operations against our current in-use index.
```shell script
cd /fp/example_devpi
devpi upload

# Verify uploaded
devpi list example_devpi

# Change version
echo '__version__ = "0.2.0"' > example_devpi.py
devpi upload

# Verify 2 versions
devpi list example_devpi
```
## Removing Release File/Project
The following only work from volatile indexes. This is a safeguard to prevent deleting production indexes

```shell script
# Remove Version
devpi remove -y example_devpi==0.2.0
devpi list example_devpi

# Remove Project
devpi remove -y example_devpi
devpi list example_devpi
```

## Uploading from Directory
Let’s execute a direct packaging step and then upload the resulting release file. First the typical setup.py packaging call
```shell script
python setup.py sdist
# We now have a release file in the dist directory
ls example_devpi/dist 

devpi upload --from-dir example_devpi/dist
devpi list example_devpi
```
## Push a Release File (to Another Index)
In this example, the current index is /fp/dev/ and we want to push version 0.2.0 to /fp/prod
```shell script
devpi push example_devpi==0.2.0 fp/prod
devpi list example_devpi
```