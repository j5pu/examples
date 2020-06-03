#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click


@click.command()
@click.option('--hash-type',
              type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
def digest(hash_type):
    click.echo(hash_type)


if __name__ == '__main__':
    digest()