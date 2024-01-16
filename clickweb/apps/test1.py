import click
import time
from .cli import cli, DEBUG

@cli.command()
@click.option("--delay", type=float, default=0.01, required=True, help='delay between each print line')
@click.option("--message", type=click.Choice(['Red', 'Blue']), default='Blue', required=True,
              help='Message to print.')
@click.argument("lines", default=10, type=int)
def test1_print_lines(lines, message, delay):
    "Just print lines with delay (demonstrates the output streaming to browser)"
    if DEBUG:
        click.echo("global debug set, printing some debug output")
    click.echo(f"writing: {lines} lines with delay {delay}s")
    for i in range(lines):
        click.echo(f"{message} row: {i}")
        time.sleep(delay)
