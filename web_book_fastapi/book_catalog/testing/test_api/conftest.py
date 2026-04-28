from collections.abc import Generator
import pytest
from starlette.testclient import TestClient

from web_book_fastapi.book_catalog.main import app

@pytest.fixture()
def client() -> Generator[TestClient]:
    with TestClient(app=app) as client:
        yield client