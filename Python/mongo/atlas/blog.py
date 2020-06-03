#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from client import client

# https://blog.pythonanywhere.com/178/
# create a database: .blog apunta a la database blog, y cuando se ejecute algo si no está la crea
db = client.blog

# create a collection/table "posts" and a document/row: .posts apunta a la collection/table "posts" y
#                                                        crea si no hay al crear el document/row
db.posts.insert_one({"title": "My first post", "body": "This is the body of my first blog post", "slug": "first-post"})

# add more "posts" documents/rows: Pero crea "documents" duplicados
db.posts.insert_one({"title": "Another post", "body": "Let's try another post", "slug": "another-post", "extra-data": "something"})
db.posts.insert_one({"title": "Blog Post III", "body": "The blog post is back in another summer blockbuster", "slug": "yet-another-post", "author": "John Smith"})

# inspect "posts" documents/rows
for post in client.blog.posts.find():
    print(post)
    try:
        print(f"title: {post['title']}")
    except KeyError as exc:
        print(f'Al crear entrada con Compass web sin "title" sale error')

# find/SELECT no parameters/SELECT no WHERE clause: returns cursor to iterate every document/raw in collection/table
#      Me da los que tienen "title" y además que el title es "Another post"
for post in client.blog.posts.find({"title": {"$eq": "Another post"}}):  # https://docs.mongodb.com/manual/reference/operator/query/
    print(post["body"])
