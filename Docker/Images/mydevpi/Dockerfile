# https://docs.docker.com/engine/reference/builder/

#FROM python:3.7-alpine3.8
FROM ubuntu:19.04

RUN apt-get update && apt-get install -y --no-install-recommends \
		python3-pip apt-utils python-setuptools \
		&& apt-get upgrade -y \
		&& apt-get dist-upgrade -y \
	    && rm -rf /var/lib/apt/lists/*
#RUN apk add --update gcc python3-dev libffi-dev musl-dev && \
#    pip3 wheel --wheel-dir=/srv/wheels 'devpi-server==4.8.0' 'devpi-client==4.2.0'

#FROM python:3.7-alpine3.8
#
#COPY --from=0 /srv/wheels /srv/wheels

VOLUME /srv/devpi

#RUN pip3 install --no-cache-dir --no-index --find-links=/srv/wheels devpi-server devpi-client
RUN pip3 install --no-cache-dir devpi-server devpi-client

#ENV DEVPISERVER_SERVERDIR ${DEVPISERVER_SERVERDIR:-/var/lib/devpi}
#ENV DEVPISERVER_HOST ${DEVPISERVER_HOST:-0.0.0.0}
#ENV DEVPISERVER_PORT ${DEVPISERVER_PORT:-3141}
#ENV DEVPISERVER_ROOT_PASSWORD ${DEVPISERVER_PORT:-1Zaragoza$.}

#ENV DEVPISERVER_USER ${DEVPISERVER_USER:-fp}
#ENV DEVPISERVER_PASSWORD ${DEVPISERVER_PASSWORD:-1Zaragoza$.}
#ENV DEVPISERVER_INDEX ${DEVPISERVER_INDEX:-dev}

CMD /bin/bash