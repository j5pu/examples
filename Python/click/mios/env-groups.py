#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click

@click.option('--debug/--no-debug')
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()
@click.option('--username')
def greet(username):
    click.echo('Hello %s!' % username)

# $ export GREETER_DEBUG=false
# $ export GREETER_GREET_USERNAME=John
# $ cli greet
# Debug mode is off
# Hello John!

if __name__ == '__main__':
    cli(auto_envvar_prefix='GREETER')