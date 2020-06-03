#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def touch(filename):
    """Print FILENAME if the file exists."""
    click.echo(click.format_filename(filename))


if __name__ == '__main__':
    touch()