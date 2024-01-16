import click
DEBUG = False

@click.group()
@click.option("--debug/--no-debug", help='set debug flag')
def cli(debug):
    'An example click script to test click-web'
    global DEBUG
    DEBUG = debug
