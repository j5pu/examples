from twitterscraper.user import User
from pprint import pprint
user = User()

"""
El primer if decide que poner y tiene then y else
El segundo if es filtro, solo tiene if
"""
filter = 'location'
change = 'Seguidores'
twitter_user = 'fp'
ejemplo = { (change if key == 'followers' else key):(twitter_user if key == 'user' else value)
            for key, value in User().__dict__.items() if key != filter}

user_info = {key: (twitter_user if key == 'user' else value) for key, value in User().__dict__.items()}

print(type(user_info))
pprint(user.__dict__)
pprint(user_info)
pprint(ejemplo)

outer_dict = {"outer_hello": {"hello": "hola"}, "outer_bye": {"bye", "adios"} }
def myfunc(message):
    return message

data = {outer_k: {inner_k: myfunc(inner_v) for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in outer_dict.items()}
