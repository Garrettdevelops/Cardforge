import click 
from flashcard.core.run import run

@click.command()
@click.option('--input', prompt='Which file should I run?')

def main(input):
    """Flashcard program that takes a CSV and creates a flashcard""" 
    run(input)

if __name__ == "__main__":
    main()
