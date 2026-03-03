from api.api_v1.movies.storage import Storage
from book_catalog.schemas.movie import Movie
from typing import Annotated
from fastapi import (Depends,
                     HTTPException,
                     status,
                     Request)
from core.config import USER_DB
from fastapi.security import HTTPBasic, HTTPBasicCredentials


UNSAFE_METHODS = frozenset(
    {
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
    }
)

storage = Storage()

user_auth = HTTPBasic(
    scheme_name="user auth",
    description="Enter your **username** and ***password*** here.",
    auto_error=False,
)

def get_storage() -> Storage:
    return storage

def basic_user_auth(
    request: Request,
    credentials: Annotated[
        HTTPBasicCredentials | None,
        Depends(user_auth),
    ] = None,
):
    if request.method not in UNSAFE_METHODS:
        return

    if (credentials
            and credentials.username in USER_DB
            and credentials.password == USER_DB[credentials.username]):
        return

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )

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
        headers={
            "WWW-Authenticate": "Basic",
        },
    )