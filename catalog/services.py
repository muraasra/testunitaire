from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Loan, Book
_LOAN_PERIOD = timedelta(days=21)

def borrow_book(book: Book, user):
    if book.available_copies <= 0:
        raise ValidationError("Aucun exemplaire disponible.")
    loan = Loan.objects.create(
        book=book,
        borrower=user,
        due_date=timezone.now().date() + _LOAN_PERIOD,
    )
    book.available_copies -= 1
    book.save(update_fields=["available_copies"])
    return loan

def return_book(loan: Loan):
    loan.mark_returned()
    book = loan.book
    book.available_copies += 1
    book.save(update_fields=["available_copies"])
    return loan