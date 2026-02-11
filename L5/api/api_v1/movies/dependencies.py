from api.api_v1.movies.storage import Storage
from book_catalog.schemas.movie import Movie
from typing import Annotated
from fastapi import Depends, HTTPException, status


storage = Storage()


def get_storage() -> Storage:
    return storage

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