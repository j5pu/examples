#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
import os
print('-------------------------')

print(os.environ)
print('-------------------------')
print(type(os.environ))
print('-------------------------')
print(os.environ)

print('-------------------------')

pprint(dict(os.environ))

print('-------------------------')
## igual no excluir __PYVENV_LAUNCHER__, si porque no en shell --- pero si que hay que saber que python usar!
exclude = ['LC_CTYPE', 'PATH', 'PS1', 'PYCHARM_DISPLAY_PORT', 'PYCHARM_HOSTED', 'SSH_AUTH_SOCK', 'TMPDIR',
           'VERSIONER_PYTHON_VERSION', 'VIRTUAL_ENV', 'XPC_FLAGS', 'XPC_SERVICE_NAME', '__CF_USER_TEXT_ENCODING',
           '__PYVENV_LAUNCHER__', '_', 'PWD', 'OLDPWD', 'SHLVL', 'TERM', 'TERMINAL_EMULATOR', 'SHELL=',
           'SHELL', 'XPC_FLAGS', 'MAIL', 'SUDO_UID', 'USERNAME', 'LOGNAME', 'SUDO_USER', 'SUDO_COMMAND', 'SUDO_GID']
environment = {key: value for key, value in dict(os.environ).items() if key not in exclude}
pprint(environment)
print('-------------------------')
for key, value in dict(os.environ).items():
    print(key + ': ' + value)
print('-------------------------')
print('-------------------------')
