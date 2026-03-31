from pydantic import BaseModel
from redis import Redis
from book_catalog.core import config
from book_catalog.schemas.book import Book, BookCreate, BookUpdate, BookPartialUpdate


redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    db=config.REDIS_DB_BOOKS,
    decode_responses=True,
)

class BooksStorage(BaseModel):
    slug_to_book: dict[str, Book] = {}

    def save_book(self, book: Book):
        redis.hset(
            config.REDIS_BOOKS_HASH_NAME,
            book.slug,
            book.model_dump_json(),
        )

    def get(self) -> list[Book]:
        books = redis.hvals(config.REDIS_BOOKS_HASH_NAME)

        result = []
        for book in books:
            result.append(
                Book.model_validate_json(book)
            )

        return result

    def get_by_slug(self, slug: str) -> Book | None:
        book_json = redis.hget(config.REDIS_BOOKS_HASH_NAME, slug)
        if not book_json:
            return None

        return Book.model_validate_json(book_json)

    def create(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        self.save_book(book)
        return book

    def delete_by_slug(self, slug: str) -> None:
        redis.hdel(config.REDIS_BOOKS_HASH_NAME, slug)

    def delete(self, book: Book) -> None:
        self.delete_by_slug(slug=book.slug)

    def update(
        self,
        book: Book,
        book_in: BookUpdate,
    ) -> Book:
        for field, value in book_in:
            setattr(book, field, value)
        self.save_book(book)
        return book

    def partial_update(
        self,
        book: Book,
        book_in: BookPartialUpdate,
    ) -> Book:
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)
        self.save_book(book)
        return book


storage = BooksStorage()


storage.create(
    BookCreate(
        title="Harry Potter",
        slug="harry",
        description="Some description",
        pages=400,
    )
)

storage.create(
    BookCreate(
        title="Lord's of the ring",
        slug="ring",
        description="Some description",
        pages=800,
    )
)
