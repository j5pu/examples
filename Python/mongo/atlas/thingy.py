#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://mongo-thingy.readthedocs.io/#complete-information-with-properties
from mongo_thingy import connect, Thingy

password = "1Zaragoza$."
encode = {"$": "%24", ".": "%2E"}
# Connect
connection = "mongodb+srv://fp:1Zaragoza%24%2E@atlas0-mzvey.mongodb.net/test?retryWrites=true&w=majority"
connect(connection)


# Insert and and find thingies
class User(Thingy):
    pass


user = User({"name": "Mr. Foo", "age": 42}).save()
print(User.count())

print(User.find_one({"age": 42}))

# Update a thingy
print(user.age)
user.age = 1337
print(user.save())
print(user.age)


# Views: Complete information with properties
class User(Thingy):
    @property
    def username(self):
        return "".join(char for char in self.name if char.isalpha())

User.add_view(name="everything", defaults=True, include="username")
user = User.find_one()
print(user.view("everything"))

# https://www.coursera.org/lecture/introduction-mongodb/welcome-11oeE?authMode=login