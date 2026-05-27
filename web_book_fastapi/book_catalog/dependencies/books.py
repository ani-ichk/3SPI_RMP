from typing import Annotated
from fastapi import Depends, Request

from storage.books import BooksStorage


def get_book_storage(
        request: Request,
) -> BooksStorage:
    return request.app.state.books_storage


GetBooksStorage = Annotated[
    BooksStorage,
    Depends(get_book_storage)
]