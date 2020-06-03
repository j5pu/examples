#!/usr/bin/env bash
# current devpi index: http://0.0.0.0:3141/root/pypi
URL=http://localhost:3141/root/pypi/+simple/
URL=http://devpi.vpn:3141/root/pypi/+simple/

URL=http://devpi.vpn:3141/root/pypi/+simple/

URL=http://devpi.vpn:51000/root/pypi/+simple/
URL=http://localhost:51000/root/pypi/+simple/

pip3 install --trusted-host devpi.vpn -i $URL simplejson
pip3 install  -i $URL simplejson
pip install  -i $URL simplejson

devpi use http://devpi.vpn:3141
devpi use http://localhost:3141

exit
devpi login root --password 1Zaragoza$.
devpi index -l

devpi-server --serverdir --init
ls -la /var/lib/devpi/.nodeinfo
ls -la ~/.devpi/server

rm /var/lib/devpi/.nodeinfo
cat /var/lib/devpi/.nodeinfo

ls -la /srv/devpi
devpi-server --start --init
devpi-server --stop

 y reinicio contenedor y deberia cambiar
docker build -t devpi_zzzspchi_alpine . && docker run -p 51000:3141 -v /var/cache/devpi_zzz:/srv/devpi --env DEVPISERVER_ROOT_PASSWORD=1Zaragoza$. --name devpi_zzzspchi_alpine -t -i --restart always --network attached devpi_zzzspchi_alpine
01e74d558c1848c39f6050b14da104fd
docker container stop devpi_zzzspchi_alpine

docker container stop devpi_zzzspchi_alpine

13986c8769d84768830431a43662a2d2

devpi use http://localhost:3141/root/pypi

devpi-server --log

docker run -d --name devpi \
    --publish 3141:3141 \
    --volume /srv/docker/devpi:/data \
    --env=DEVPI_PASSWORD=1Zaragoza$. \
    --restart always \
    muccg/devpi

  twine upload --repository http://devpi.vpn:3141/root/dev -u root -p ""