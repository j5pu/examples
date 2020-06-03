#!/usr/bin/env bash
# current devpi index: http://0.0.0.0:3141/root/pypi
URL=http://localhost:3141/root/pypi/+simple/

URL=http://devpi.vpn:51000/root/pypi/+simple/
URL=http://localhost:51000/root/pypi/+simple/

pip3 install -I $URL simplejson
