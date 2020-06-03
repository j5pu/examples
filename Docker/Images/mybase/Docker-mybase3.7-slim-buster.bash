#!/usr/bin/bash

docker build --file Docker-mybase3.7-slim-buster --network attached -t $REGISTRY/mybase3.7:slim-buster .
docker push $REGISTRY/mybase3.7:slim-buster
