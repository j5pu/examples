#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import click
@click.command()
@click.argument('input', type=click.File('rb'))
@click.argument('output', type=click.File('wb'))
def inout(input, output):
    """Copy contents of INPUT to OUTPUT."""
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(chunk)
if __name__ == '__main__':
    inout()