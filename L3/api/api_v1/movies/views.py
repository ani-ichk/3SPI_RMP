from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)


from book_catalog.schemas.movie import Movie, MovieCreate
from api.api_v1.movies.crud import MOVIES
from api.api_v1.movies.dependencies import prefetch_movie


router = APIRouter(tags=["Movies"])

@router.get(
    "/movies",
    response_model=list[Movie],
)
def get_list_movies():
    return MOVIES


@router.post(
    "/movies",
    response_model=Movie,
)
def create_movie(movie_in: MovieCreate) -> Movie:
    return Movie(**movie_in.model_dump())



@router.get("/movies/{slug}")
def get_movie_details_by_slug(
    movie: Annotated[
        Movie,
        Depends(prefetch_movie),
    ],
) -> Movie | None:
    return movie