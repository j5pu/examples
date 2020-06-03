#!/usr/bin/env bash

VARIABLE=
[[ ${VARIABLE-} ]] && echo Llena || echo Vacia

VARIABLE=2
[[ ${VARIABLE-} ]] && echo Llena || echo Vacia

VARIABLE=
[[ ${VARIABLE:-} ]] && echo Llena || echo Vacia

VARIABLE=2
[[ ${VARIABLE:-} ]] && echo Llena || echo Vacia