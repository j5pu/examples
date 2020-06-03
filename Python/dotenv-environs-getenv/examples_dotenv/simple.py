#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("--------------- load")
from dotenv import load_dotenv
load_dotenv()
print(load_dotenv(verbose=True))
print("--------------- Path")
from pathlib import Path  # python3 only

path = Path('.')
print(path)

env_path = Path('.') / '.env'
print(env_path)
print(load_dotenv(dotenv_path=env_path, verbose=True))
print("--------------- getenv")

import os
SECRET_KEY = os.getenv("PASSWD_ENCODED")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

print("--------------- find_dotenv")

from dotenv import load_dotenv, find_dotenv

print(find_dotenv())
print(load_dotenv(find_dotenv(), verbose=True))

print("--------------- dotenv_values")
from dotenv import dotenv_values
values = dotenv_values(verbose=True)
print(values)

print("--------------- get_key ")
from dotenv import get_key


PASSWD_ENCODED = get_key(find_dotenv(), 'PASSWD_ENCODED')
print(PASSWD_ENCODED)

print("--------------- set_key ")
from dotenv import set_key

print(set_key(find_dotenv(), 'A', '30', quote_mode="never"))
print(set_key(find_dotenv(), 'HOME', '${HOME}', quote_mode="never"))

A = get_key(find_dotenv(), 'A')
print(A)

print("--------------- unset_key ")
from dotenv import set_key
# set_key, unset_key