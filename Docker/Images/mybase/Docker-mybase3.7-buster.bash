#!/usr/bin/bash

docker build --file Docker-mybase3.7-buster --network attached -t $REGISTRY/mybase3.7:buster .
docker push $REGISTRY/mybase3.7:buster
