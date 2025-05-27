from django.urls import path, include
from . import views, api
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"books", api.BookViewSet)
router.register(r"authors", api.AuthorViewSet)
router.register(r"loans", api.LoanViewSet)
urlpatterns = [
    path("", views.BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/add/", views.BookCreateView.as_view(), name="book-add"),
    path("books/<int:pk>/edit/", views.BookUpdateView.as_view(), name="book-edit"),
    path("api/", include(router.urls)),
]