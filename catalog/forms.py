from django import forms
from .models import Author, Book
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "author", "category", "isbn", "summary", "available_copies")