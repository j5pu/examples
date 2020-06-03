#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click

## https://click.palletsprojects.com/en/7.x/parameters/
@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello(dict(name="a"))