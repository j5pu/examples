#!/usr/bin/env bash

printf '${0} is: %s\n and $( basename "${0}" ) is: %s\n' "${0}" "$( basename "${0}" )"