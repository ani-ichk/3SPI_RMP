from typing import Annotated
from fastapi import APIRouter, Depends
from book_catalog.schemas.movie import Movie, MovieCreate
from api.api_v1.movies.dependencies import get_storage
from api.api_v1.movies.storage import Storage


router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get(
    "/",
    response_model=list[Movie],
)
def get_list_movies(
    storage: Annotated[Storage, Depends(get_storage)],
):
    return storage.get_movies()


@router.post(
    "/",
    response_model=Movie,
)
def create_movie(
    movie_in: MovieCreate,
    storage: Annotated[Storage, Depends(get_storage)],
):
    return storage.create_movie(movie_in)