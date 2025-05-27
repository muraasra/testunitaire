import pytest
from django.contrib.auth.models import User
from catalog.models import Author, Book, Category
@pytest.fixture
def user(db):
    return User.objects.create_user("reader", "reader@test.com", "pass")
@pytest.fixture
def author(db):
    return Author.objects.create(first_name="Isaac", last_name="Asimov")
@pytest.fixture
def category(db):
    return Category.objects.create(name="SF")
@pytest.fixture
def book(db, author, category):
    return Book.objects.create(title="Foundation", author=author, category=category, isbn="9780553382563")