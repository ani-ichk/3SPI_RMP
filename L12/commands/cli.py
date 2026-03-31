import typer
from commands.hello import hello_app


app = typer.Typer(
    rich_markup_mode="rich"
)

@app.callback()
def callback():
    """
    Some CLI management commands.
    """

app.add_typer(
    hello_app,
)