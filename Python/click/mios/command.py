import click

@click.command()
def command():
    click.echo('Hello World!')

if __name__ == '__main__':
    command()