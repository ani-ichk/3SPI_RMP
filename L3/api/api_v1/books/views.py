from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)

from book_catalog.schemas.book import Book, BookCreate
from api.api_v1.books.crud import BOOKS
from api.api_v1.books.dependencies import  prefetch_book


router = APIRouter(tags=["Books"])

@router.get(
    "/books",
    response_model=list[Book],
)
def get_books():
    return BOOKS

@router.post(
    "/books",
    response_model=Book,
)
def create_book(book_in: BookCreate) -> Book:
    return Book(**book_in.model_dump())


@router.get("/books/{slug}")
def get_book_details_by_slug(
    book: Annotated[
        Book,
        Depends(prefetch_book),
    ],
) -> Book | None:
    return book