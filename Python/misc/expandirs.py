#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = "${HOME}/test/testing"
print(os.path.expandvars(path))

path = "~/test/testing"
print(os.path.expandvars(path))


path = "${USUARIO:-${USER}}/test/testing"
print(os.path.expandvars(path))
path = "~/test/testing"
print(os.path.expanduser(path))