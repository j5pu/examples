#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_pymongo import PyMongo
from client import url

app = Flask(__name__)

# /blog creada en app.py
app.config["MONGO_URI"] = url + "/blog" + "?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template("blog.html", posts=mongo.db.posts.find())

@app.route('/<post_slug>')
def item(post_slug):
    # The only really new thing is the abbreviated syntax for searching for an exact match
    #     antes era: posts.find({"title": {"$eq": "Another post"}})
    #     y ahora es equivalente a: posts.find({"slug": {"$eq": post_slug}}),
    #     en http://localhost/another-post pone "another-post" en post_slug
    return render_template("blog.html", posts=mongo.db.posts.find({"slug": post_slug}))