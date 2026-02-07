from book_catalog.schemas.movie import Movie
from api.api_v1.movies.crud import MOVIES
from fastapi import (
    HTTPException,
    status,
)


def prefetch_movie(slug: str) -> Movie:
    movie: Movie | None = next(
        (movie for movie in MOVIES if movie.slug == slug),
        None,
    )
    if movie:
        return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )