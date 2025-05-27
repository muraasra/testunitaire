from rest_framework import serializers
from .models import Book, Author, Loan
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), source="author", write_only=True)
    class Meta:
        model = Book
        fields = ("id", "title", "author", "author_id", "category", "isbn", "summary", "available_copies")
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"