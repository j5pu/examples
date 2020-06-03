#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from environs import Env
import json
from pprint import pprint
# with open(".env.test", "w") as fobj:
#     fobj.write("A=foo\n")
#     fobj.write("B=123\n")

env = Env()
env.read_env(".env.test", recurse=False)

assert env("A") == "foo"
assert env.int("B") == 12

with open('to.json', 'w') as outfile:
    json.dump(env.dump(), outfile)

pprint(env.dump(), indent=2)