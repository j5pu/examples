#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click

@click.command()
@click.option('--name', prompt='Your name please')
def hello(name):
    click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()