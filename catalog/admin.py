# Django admin configuration for the catalog app
from django.contrib import admin
from .models import Author, Book, Loan, Category
admin.site.register((Author, Book, Loan, Category))