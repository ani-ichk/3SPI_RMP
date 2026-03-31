import typer
from typing import Annotated
from rich import print


hello_app = typer.Typer(
    rich_markup_mode="rich",
    help="[red]Greet[/red] user by [bold]name[/bold].",
)

@hello_app.command(
)
def hello(
        name: Annotated[
            str,
            typer.Argument(help="Name to greet"),
        ],
):
    print(f"Hello, [bold][green]{name}[/green][/bold]!")