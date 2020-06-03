#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
import os

@click.command()
@click.option('--username')
def greet(username):
    click.echo('Hello %s!' % username)

if __name__ == '__main__':
    greet(auto_envvar_prefix='GREETER')
# $ export GREETER_USERNAME=john
# $ greet

if __name__ == '__main__':
    greet()