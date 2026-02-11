from book_catalog.schemas.movie import Movie, MovieCreate, MovieUpdate, MoviePartialUpdate


class Storage:
    def __init__(self):
        self.movies: list[Movie] = []

    def get_movies(self) -> list[Movie]:
        return self.movies

    def create_movie(self, movie_in: MovieCreate) -> Movie:
        movie = Movie(**movie_in.model_dump())
        self.movies.append(movie)
        return movie

    def delete_movie(self, movie: Movie) -> None:
        self.movies.remove(movie)

    def update_movie(
        self,
        movie: Movie,
        movie_in: MovieUpdate,
    ) -> Movie:
        for key, value in movie_in.model_dump().items():
            setattr(movie, key, value)
        return movie

    def partial_update_movie(
        self,
        movie: Movie,
        movie_in: MoviePartialUpdate,
    ) -> Movie:
        for key, value in movie_in.model_dump(exclude_unset=True).items():
            setattr(movie, key, value)
        return movie