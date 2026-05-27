from unittest import TestCase
import random
from collections.abc import Generator
import pytest

from storage.books.crud import storage, BookAlreadyExistsError
from web_book_fastapi.book_catalog.api.api_v1.books.views.list_views import create_book
from web_book_fastapi.book_catalog.schemas.book import BookCreate, BookUpdate, Book


def total(num_a,num_b):
    return num_a + num_b


class TotalTestcase(TestCase):

    def test_total(self) -> None:
        num_a = random.randint(1,100)
        num_b = random.randint(1,100)
        result = total(num_a,num_b)
        expected_result = num_a + num_b
        self.assertEqual(expected_result, result)


class BooksStorageUpdateTestcase(TestCase):
    def setUp(self):
        self.book = self.create_book()

    def create_book(self):
        book_in = BookCreate(
            slug='some_slug',
            title='title',
            description='description',
            pages=123
        )
        return storage.create(book_in)

    def test_update(self):
        book_update = BookUpdate(
            **self.book.model_dump(),
        )
        source_description = self.book.description
        book_update.description *= 2
        updated_book = storage.update(
            book=self.book,
            book_in=book_update,
        )

        self.assertNotEqual(source_description, updated_book.description)
        self.assertEqual(book_update.description, updated_book.description)

    def test_partial_update(self):
        book_update = BookUpdate(title='new title')
        updated_book = storage.update(
            book=self.book,
            book_in=book_update,
        )
        self.assertEqual(updated_book.title, 'new title')
        self.assertEqual(updated_book.description, self.book.description)

    def tearDown(self):
        storage.delete(self.book)


class BooksStorageGlobalTestcase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_slugs = ['slug_1', 'slug_2']
        cls.created_books = []
        for slug in cls.test_slugs:
            book_in = BookCreate(
                slug=slug,
                title='title',
                description='description',
                pages=123
            )
            book = storage.create(book_in)
            cls.created_books.append(book)

    @classmethod
    def tearDownClass(cls):
        for book in cls.created_books:
            storage.delete(book)

    def test_get_list(self):
        all_books = storage.get()
        slugs_in_db = [book.slug for book in all_books]
        for slug in self.test_slugs:
            with self.subTest(slug=slug):
                self.assertIn(slug, slugs_in_db)

    def test_get_by_slug(self):
        for book in self.created_books:
            with self.subTest(slug=book.slug):
                found_book = storage.get_by_slug(book.slug)
                self.assertIsInstance(found_book.title, book.title)


def test_create_or_raise_if_exists(book: Book) -> None:
    #existing_book = create_book()
    book_create = BookCreate(**book.model_dump())
    with pytest.raises(BookAlreadyExistsError) as exc_info:
        storage.create_or_raise_if_exists(book_create)

    assert exc_info.value.args[0] == book_create.slug

@pytest.fixture()
def book() -> Generator[Book]:
    book = create_book()
    yield book
    storage.delete(book)