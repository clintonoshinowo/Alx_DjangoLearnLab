# relationships_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

# Import all necessary models and forms from your project
from .models import Book, Author, Publisher, Library, Librarian, UserProfile
from .forms import BookForm

def index(request):
    """
    A simple index view that provides a welcome message.
    """
    return HttpResponse("Welcome to the Relationship App! This is the home page.")

def register(request):
    """
    Placeholder view for a user registration page.
    """
    return HttpResponse("This is the user registration page.")

# Simple view to list all books
def list_books(request):
    """
    Renders a simple page listing all books.
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationships_app/list_books.html', context)

# Simple placeholder view for the librarian page
def librarian_view(request):
    """
    Placeholder view for the librarian page.
    """
    return HttpResponse("Welcome, Librarian! This is your special page.")

# This is the new, integrated view for adding a book.
# It uses a class to handle both displaying and processing the form.
class AddBookView(LoginRequiredMixin, View):
    """
    A class-based view to handle the creation of new books.
    It uses the BookForm to render the form and process form submissions.
    """
    def get(self, request):
        """
        Handles GET requests to display an empty form.
        """
        form = BookForm()
        return render(request, 'relationships_app/add_book.html', {'form': form})

    def post(self, request):
        """
        Handles POST requests when the user submits the form.
        """
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Remember to replace this with your desired URL name
        
        return render(request, 'relationships_app/add_book.html', {'form': form})

# The following views are secured using the permission_required decorator.
# We will keep these as function-based views.

@permission_required('relationships_app.can_change_book', raise_exception=True)
def change_book(request, pk):
    """
    View for changing an existing book.
    """
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You have permission to change the book: {book.title}")

@permission_required('relationships_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    """
    View for deleting a book.
    """
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"You have permission to delete the book: {book.title}")

