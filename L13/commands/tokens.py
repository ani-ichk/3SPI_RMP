import typer
from typing import Annotated
from rich import print
from rich.markdown import Markdown

from book_catalog.api.api_v1.auth.services.redis_tokens_halper import RedisTokensHelper

tokens_app = typer.Typer(
    rich_markup_mode="rich",
    help="Token management commands",
    name="token",
)

@tokens_app.command()
def check(
        token: Annotated[
            str,
            typer.Argument(help="The token to check"),
        ],
):
    redis_tokens = RedisTokensHelper()

    if redis_tokens.token_exists(token):
        print(f"Token {token} [green]exists[/green]")
    else:
        print(f"Token {token} [red]does not exist[/red]")

@tokens_app.command()
def list():
    redis_tokens = RedisTokensHelper()
    tokens = redis_tokens.get_tokens()
    text = "*Available API Tokens*\n"
    for token in tokens:
        text += f"- {token}\n"
    print(Markdown(text))

@tokens_app.command()
def create():
    redis_tokens = RedisTokensHelper()
    tokens = redis_tokens.generate_and_save_token()
    print(f"[green]Created new token[/green]: {tokens}")

@tokens_app.command()
def add(
        token: Annotated[
            str,
            typer.Argument(help="The token to add"),
        ],
):
    redis_tokens = RedisTokensHelper()
    redis_tokens.add_token(token)
    print(f"[green]Added new token [/green]: {token}")

@tokens_app.command()
def rm(
        token: Annotated[
            str,
            typer.Argument(help="The token to remove"),
        ],
):
    redis_tokens = RedisTokensHelper()
    redis_tokens.delete_token(token)

    print(f"[green]Removed token [/green]: {token}")