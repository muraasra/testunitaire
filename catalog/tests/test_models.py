from catalog.models import Loan
from catalog.services import borrow_book

def test_borrow_decrements_stock(book, user):
    start = book.available_copies
    loan = borrow_book(book, user)
    assert loan.book == book
    book.refresh_from_db()
    assert book.available_copies == start - 1