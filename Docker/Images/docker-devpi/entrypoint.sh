#!/bin/sh

# Restart Nginx proxy to load devpi configuration.
/etc/init.d/nginx restart

# Initialize the devpi index, if it isn't already.
sudo -Hu devpi devpi-server --init

# Start devpi-server.
sudo -Hu devpi devpi-server --host=0.0.0.0 --port=8000
