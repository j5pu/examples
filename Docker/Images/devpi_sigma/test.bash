#!/usr/bin/env bash
# current devpi index: http://0.0.0.0:3141/root/pypi

# TEST
URL=http://localhost:3141/root/pypi/+simple/


# MAC
URL=http://devpi.vpn:3141/root/pypi/+simple/

pip3 install --trusted-host devpi.vpn -i $URL simplejson


python3 -m pip install --upgrade --trusted-host -i $URL setuptools wheel

pip3 install --upgrade --trusted-host devpi.vpn -i $URL devpi-client
python3 setup.py sdist bdist_wheel

devpi use http://devpi.vpn:3141
devpi login root --password=""
devpi index -l
devpi index -c dev bases=root/pypi
devpi use root/dev
cd import_getenv && devpi upload
devpi install import_getenv
pip3 install --trusted-host devpi.vpn -i $URL import_getenv


/etc/pip.conf          : no config file exists
~/.pydistutils.cfg     : no config file exists
~/.buildout/default.cfg: no config file exists