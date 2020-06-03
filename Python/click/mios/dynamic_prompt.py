#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import os

@click.command()
@click.option('--username', prompt=True,
              default=lambda: os.environ.get('USER', ''))
def hello(username):
    print("Hello,", username)

# show_default permite preguntar si coge la de ambiente

# @click.command()
# @click.option('--username', prompt=True,
#               default=lambda: os.environ.get('USER', ''),
#               show_default='current user')
# def hello(username):
#     print("Hello,", username)

if __name__ == '__main__':
    hello()