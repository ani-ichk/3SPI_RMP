from web_book_fastapi.book_catalog.schemas.book import Book, BookCreate, BookUpdate, BookPartialUpdate
from unittest import TestCase


class BookCreateTestCase(TestCase):
    def test_book_can_be_created_from_create_schemas(self):
        book_in = BookCreate(
            slug='some-slug',
            title='title',
            description='description',
            pages=123,
        )
        book = Book(**book_in.model_dump())

        self.assertEqual(book_in.slug, book.slug)
        self.assertEqual(book_in.title, book.title)
        self.assertEqual(book_in.description, book.description)
        self.assertEqual(book_in.pages, book.pages)

    def test_book_create_accepts_different_slug(self):
        slugs = [
            "some-slug",
            "s",
            "new",
            "new-some-slug-some-slug-some-slug",
        ]
        for slug in slugs:
            with self.subTest(slug=slug, msg=f"slug {slug}"):
                book_in = BookCreate(
                    slug=slug,
                    title='title',
                    description='description',
                    pages=123,
                )
                self.assertEqual(slug, book_in.slug)

    def test_book_base_pages(self):
        pages_list = [100, 125.5, 10, 12.55]
        for pages in pages_list:
            with self.subTest(pages=pages, msg=f"pages {pages}"):
                if isinstance(pages, int):
                    book_in = BookCreate(
                        slug='some-slug',
                        title='title',
                        description='description',
                        pages=pages,
                    )
                    self.assertEqual(pages, book_in.pages)
                elif isinstance(pages, float):
                    with self.assertRaises(ValueError):
                        BookCreate(
                            slug='some-slug',
                            title='title',
                            description='description',
                            pages=pages,
                        )


class BookUpdateTestCase(TestCase):
    def test_book_updated(self):
        book = Book(
            slug='some-slug',
            title='title',
            description='description',
            pages=123,
        )
        book_in = BookUpdate(
            title='new-title',
            description='new-description',
            pages=125,
        )
        for field, value in book_in:
            setattr(book, field, value)

        self.assertEqual(book_in.title, book.title)
        self.assertEqual(book_in.description, book.description)
        self.assertEqual(book_in.pages, book.pages)


class BookPartialUpdateTestCase(TestCase):
    def test_book_partial_updated_title(self):
        source_description = 'description'
        source_pages = 123

        book = Book(
            slug='some-slug',
            title='title',
            description=source_description,
            pages=source_pages,
        )
        book_in = BookPartialUpdate(
            title='new-title',
        )
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book_in.title, book.title)

        self.assertEqual(source_description, book.description)
        self.assertEqual(source_pages, book.pages)

    def test_book_partial_updated_description(self):
        source_title = 'title'
        source_pages = 123

        book = Book(
            slug='some-slug',
            title=source_title,
            description='description',
            pages=source_pages,
        )
        book_in = BookPartialUpdate(
            description='new-description',
        )
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book_in.description, book.description)

        self.assertEqual(source_title, book.title)
        self.assertEqual(source_pages, book.pages)

    def test_book_partial_updated_pages(self):
        source_title = 'title'
        source_description = 'description'

        book = Book(
            slug='some-slug',
            title=source_title,
            description=source_description,
            pages=123,
        )
        book_in = BookPartialUpdate(
            pages=125,
        )
        for field, value in book_in.model_dump(exclude_unset=True).items():
            setattr(book, field, value)

        self.assertEqual(book_in.pages, book.pages)

        self.assertEqual(source_title, book.title)
        self.assertEqual(source_description, book.description)