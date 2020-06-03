import click

@click.group()
def cli():
    pass

@click.command()
def initdb():
    click.echo('Initialized the database')

@click.command()
def dropdb():
    click.echo('Dropped the database')

cli.add_command(initdb)
cli.add_command(dropdb)

@click.group()
def cli1():
    pass

@cli1.command()
def initdb():
    click.echo('Initialized the database')

@cli1.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()
    exit()
    cli1()