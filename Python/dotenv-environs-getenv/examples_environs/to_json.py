import os
import json
from pprint import pprint

from environs import Env


os.environ["GITHUB_USER"] = "sloria"
os.environ["API_KEY"] = "123abc"
os.environ["SHIP_DATE"] = "1984-06-25"
os.environ["ENABLE_LOGIN"] = "true"
os.environ["MAX_CONNECTIONS"] = "42"
os.environ["GITHUB_REPOS"] = "webargs,konch,ped"
os.environ["COORDINATES"] = "23.3,50.0"



env = Env()
env.read_env()
env.read_env(".env.test", recurse=False)
print(env.dump())

env = Env()
env.read_env(".env.test", recurse=False)
print(env.dump())


# json.load(env.dump())
with open('env_to.json', 'w') as outfile:
    json.dump(env.dump(), outfile)

pprint(env.dump(), indent=2)
