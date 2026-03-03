from api.api_v1.movies.storage import Storage
from book_catalog.schemas.movie import Movie
from typing import Annotated
from fastapi import (Depends,
                     HTTPException,
                     status,
                     Request,
                     Query,
                     Header)
from core.config import API_TOKENS


UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)

storage = Storage()

def get_storage() -> Storage:
    return storage

def verify_api_token(
    request: Request,
    api_token: Annotated[
        str | None,
        Query(),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if not api_token or api_token not in API_TOKENS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API token",
        )

# def verify_api_token(
#     request: Request,
#     api_token: Annotated[
#         str | None,
#         Header(alias="x-auth-token"),
#     ] = None,
# ):
#     if request.method not in UNSAFE_METHODS:
#         return
#
#     if not api_token or api_token not in API_TOKENS:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid or missing API token",
#         )

def get_movie_by_slug(
    slug: str,
    storage: Annotated[Storage, Depends(get_storage)],
) -> Movie:
    movie = next(
        (movie for movie in storage.movies if movie.slug == slug),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )