import click 
from flashcard.core.run import run_flashcards
from flashcard.core.importer import build_deck 

@click.group()
def cli():
    pass

@click.command()
@click.argument("csv_file")
def init(csv_file):
    build_deck(csv_file)

@click.command()
@click.option('--input', prompt='Which file should I run?')

def run(input):
    """Flashcard program that takes a CSV and creates a flashcard""" 
    run_flashcards(input)
    return

cli.add_command(init)
cli.add_command(run)

def main():
    cli()

if __name__ == "__main__":
    main()



