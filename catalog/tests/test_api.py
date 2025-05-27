import pytest
from rest_framework.test import APIClient
@pytest.mark.django_db
def test_book_list(book):
    client = APIClient()
    resp = client.get("/api/books/")
    assert resp.status_code == 200
    assert resp.data[0]["title"] == book.title