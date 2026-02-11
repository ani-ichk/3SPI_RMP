from book_catalog.schemas.book import Book
from api.api_v1.books.crud import BOOKS

from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Depends,
)


def prefetch_book(slug: str) -> Book:
    book: Book | None = next(
        (book for book in BOOKS if book.slug == slug),
        None,
    )
    if book:
        return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Slug {slug!r} not found",
    )