from book_catalog.schemas.movie import Movie, MovieCreate
from fastapi import HTTPException, status


class Storage:
    def __init__(self):
        self.movies: list[Movie] = []

    def get_movies(self) -> list[Movie]:
        return self.movies

    def get_movie_by_slug(self, slug: str) -> Movie:
        movie: Movie | None = next(
            (movie for movie in self.movies if movie.slug == slug),
            None,
        )
        if movie:
            return movie
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Slug {slug!r} not found",
        )

    def create_movie(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(**movie_in.model_dump())
        self.movies.append(movie)
        return movie