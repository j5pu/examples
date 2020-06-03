#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient

password = "1Zaragoza$."
encode = {"$": "%24", ".": "%2E"}
# Connect
# connection = "mongodb+srv://fp:1Zaragoza%24%2E>@atlas0-mzvey.mongodb.net/test?retryWrites=true&w=majority"
# connect(connection)

# client = MongoClient("mongodb+srv://fp:1Zaragoza%24%2E@atlas0-mzvey.mongodb.net/test?retryWrites=true&w=majority")
url = "mongodb+srv://fp:1Zaragoza%24%2E@atlas0-mzvey.mongodb.net"
client = MongoClient(url + "/admin")

print(client.get_default_database())
print(client.list_database_names())

# for name in client.list_database_names():
#     client.drop_database(name)
print(client.list_database_names())
