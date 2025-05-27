from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    def _str_(self):
        return f"{self.last_name}, {self.first_name}"

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def _str_(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    summary = models.TextField(blank=True)
    available_copies = models.PositiveIntegerField(default=1)
    def _str_(self):
        return self.title

class Loan(models.Model):
    STATUS_CHOICES = (
        ("on_loan", "En prêt"),
        ("returned", "Retourné"),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="on_loan")
    start_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    class Meta:
        unique_together = ("book", "borrower", "status")
    def _str_(self):
        return f"{self.book} -> {self.borrower} ({self.status})"
    def mark_returned(self):
        self.status = "returned"
        self.returned_date = timezone.now().date()
        self.save()