from typing import Annotated

from fastapi import APIRouter, Depends, status

from book_catalog.schemas.movie import (
    Movie,
    MovieUpdate,
    MoviePartialUpdate,
)
from api.api_v1.movies.dependencies import (
    get_storage,
    get_movie_by_slug,
)
from api.api_v1.movies.storage import Storage


router = APIRouter(
    prefix="/movies/{slug}",
    tags=["Movies"],
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Movie not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Slug 'movie-slug' not found"}
                }
            },
        }
    },
)


movie_dependency = Annotated[Movie, Depends(get_movie_by_slug)]
storage_dependency = Annotated[Storage, Depends(get_storage)]


@router.get(
    "/",
    response_model=Movie,
)
def get_movie_details(
    movie: movie_dependency,
):
    return movie


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_movie(
    movie: movie_dependency,
    storage: storage_dependency,
):
    storage.delete_movie(movie)


@router.put(
    "/",
    response_model=Movie,
)
def update_movie(
    movie: movie_dependency,
    movie_in: MovieUpdate,
    storage: storage_dependency,
):
    return storage.update_movie(movie, movie_in)


@router.patch(
    "/",
    response_model=Movie,
)
def partial_update_movie(
    movie: movie_dependency,
    movie_in: MoviePartialUpdate,
    storage: storage_dependency,
):
    return storage.partial_update_movie(movie, movie_in)
