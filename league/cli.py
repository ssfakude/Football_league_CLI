import click
from colorama import Fore
from .svc_football import football_legaue
import os.path

default_file = os.path.join("league", "input.txt")

@click.command()
@click.option("-f", "--file_name", type=str, help="Input file name", default=default_file, show_default=True)
def cli( file_name):
    count=1
    results=football_legaue(file_name)
    if type(results) == str:
        click.echo(Fore.RED +results)
        return
    for team in results:
        click.echo(f'{count}. {team[0]}, {team[1]} pts')  
        count+=1
