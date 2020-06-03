#!/usr/bin/bash

docker build --file Docker-mybase3.7-alpine --network attached -t $REGISTRY/mybase3.7:alpine .
docker push $REGISTRY/mybase3.7:alpine
