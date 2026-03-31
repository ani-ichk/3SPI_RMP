import typer
from commands.tokens import tokens_app


app = typer.Typer(
    rich_markup_mode="rich"
)

@app.callback()
def callback():
    """
    Some CLI management commands.
    """

app.add_typer(
    tokens_app,
    name="tokens",
)