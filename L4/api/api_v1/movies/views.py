from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)


from book_catalog.schemas.movie import Movie, MovieCreate
from api.api_v1.movies.dependencies import get_storage
from api.api_v1.movies.storage import Storage


router = APIRouter(tags=["Movies"])


@router.get(
    "/movies",
    response_model=list[Movie],
)
def get_list_movies(
    storage: Annotated[Storage, Depends(get_storage)],
):
    return storage.get_movies()


@router.post(
    "/movies",
    response_model=Movie,
)
def create_movie(
    movie_in: MovieCreate,
    storage: Annotated[Storage, Depends(get_storage)],
):
    return storage.create_movie(movie_in)


@router.get(
    "/movies/{slug}",
    response_model=Movie,
)
def get_movie_details_by_slug(
    slug: str,
    storage: Annotated[Storage, Depends(get_storage)],
):
    return storage.get_movie_by_slug(slug)