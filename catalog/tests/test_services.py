import pytest
from django.core.exceptions import ValidationError
from catalog.services import borrow_book

def test_cannot_borrow_when_zero_copies(book, user):
    book.available_copies = 0
    book.save()
    with pytest.raises(ValidationError):
        borrow_book(book, user)