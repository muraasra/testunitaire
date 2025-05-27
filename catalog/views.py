from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Book, Author
from .forms import BookForm, AuthorForm
class BookListView(ListView):
    model = Book
    paginate_by = 20
class BookDetailView(DetailView):
    model = Book
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book-list")
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book-list")
# Author views analogous…