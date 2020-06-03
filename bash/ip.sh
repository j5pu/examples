#!/bin/bash

CWD="$(pwd)"
SERVICE="ip.service"
sudo ln -s "${CWD}/${SERVICE}" "/etc/systemd/system/${SERVICE}" >/dev/null 2>&1
if [[ "$1" != 'stop' ]]; then
    sudo systemctl daemon-reload
    sudo systemctl start "${SERVICE}"
else
    sudo systemctl stop "${SERVICE}"
fi