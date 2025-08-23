from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book

# Function-based view to list all books
def list_all_books(request):
    """
    Renders a page listing all books from the database.
    """
    # Query all Book objects from the database
    books = Book.objects.all()
    # Pass the books queryset to the template context
    context = {
        'books': books
    }
    # Render the list_books.html template with the context
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to show details for a single library
class LibraryDetailView(DetailView):
    """
    Renders a page with details for a specific library, including its books.
    This view uses Django's built-in DetailView.
    """
    # The model this view will be working with
    model = Library
    # The name of the template to be rendered
    template_name = 'relationship_app/library_detail.html'
    # The name of the context object used in the template (e.g., {{ library }})
    context_object_name = 'library'

# Create your views here.
