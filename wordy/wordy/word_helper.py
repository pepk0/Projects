import click
from .functionality import validate_words

@click.command()
@click.argument("letters")
@click.option("-l", default=3, type=int)
def word_helper(letters: str, l: int):
    
    words = validate_words(letters, l)

    return click.echo(words)
