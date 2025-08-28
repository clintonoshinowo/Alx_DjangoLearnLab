# relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

# Import all necessary models from your unified models.py
from .models import Book, Author, Publisher, Library, Librarian, UserProfile

def index(request):
    """
    A simple index view that provides a welcome message.
    This view is necessary to resolve the AttributeError in your traceback.
    """
    return HttpResponse("Welcome to the Relationship App! This is the home page.")

def register(request):
    """
    Placeholder view for a user registration page.
    This view is necessary to resolve the new AttributeError.
    """
    return HttpResponse("This is the user registration page.")

# Simple view to list all books
def list_books(request):
    """
    Renders a simple page listing all books.
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Simple placeholder view for the librarian page
def librarian_view(request):
    """
    Placeholder view for the librarian page.
    """
    return HttpResponse("Welcome, Librarian! This is your special page.")

# The following views are secured using the permission_required decorator.
# The permission format is 'app_label.codename'.

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    """
    View for adding a new book. Only users with 'can_add_book' permission can access.
    """
    # For simplicity, we just return a message.
    # In a real app, you would handle a form here.
    return HttpResponse("You have permission to add a book!")

@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book(request, pk):
    """
    View for changing an existing book. Only users with 'can_change_book' permission can access.
    The 'pk' (primary key) is used to find the specific book.
    """
    # Use get_object_or_404 to get the book instance.
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You have permission to change the book: {book.title}")

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """
    View for deleting a book. Only users with 'can_delete_book' permission can access.
    The 'pk' (primary key) is used to find the specific book.
    """
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You have permission to delete the book: {book.title}")
