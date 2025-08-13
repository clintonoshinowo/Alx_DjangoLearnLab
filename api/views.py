from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# We now use a ModelViewSet for books, which combines all CRUD actions.
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Similarly, we use a ModelViewSet for authors.
class AuthorViewSet(viewsets.ModelViewSet):
    """
    A ViewSet that automatically provides all CRUD actions for the Author model.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
