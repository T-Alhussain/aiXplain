import click
from aixplain.factories.model_factory_cli import list_host_machines, list_functions

@click.group('cli')
def cli():
    pass

@click.group('list')
@click.pass_context
def list(ctx):
    pass

@click.group('get')
def get():
    pass

@click.group('create')
def create():
    pass

@click.group('onboard')
def onboard():
    pass

cli.add_command(list)
cli.add_command(get)
cli.add_command(create)
cli.add_command(onboard)

list.add_command(list_host_machines)
list.add_command(list_functions)

def run_cli():
    cli()