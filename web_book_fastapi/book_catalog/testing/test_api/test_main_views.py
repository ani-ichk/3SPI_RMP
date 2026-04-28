import pytest
from starlette.testclient import TestClient
from fastapi import status
from web_book_fastapi.book_catalog.main import app


client = TestClient(app)

def test_root_view():
    response = client.get('/')
    expected_message = f'Hello World'
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data['docs'] == '/docs'
    assert data['message'] == expected_message

@pytest.mark.parametrize(
    'name',
    [
        'BGPU',
        'Bob',
        'Boba',
        '%&!$*%'
    ],
)
def test_root_view_custom_name(name: str):
    query = {'name': name}
    response = client.get('/', params=query)
    expected_message = f'Hello {name}'
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data['docs'] == '/docs'
    assert data['message'] == expected_message
