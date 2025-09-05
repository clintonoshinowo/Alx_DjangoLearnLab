from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre, Language, Publisher
from django.db.models import Count
from django.shortcuts import HttpResponse

def homepage(request):
    """
    Renders a simple HTTP response for the homepage.
    """
    return HttpResponse("<h1>Hello, world!</h1><p>This is your new Django homepage.</p>")

def index(request):
    """
    View function for the home page of the library site.
    """
    # Number of books and authors.
    num_books = Book.objects.count()
    num_authors = Author.objects.count()

    # Number of available books (status = 'a').
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    return HttpResponse("Welcome to the Relationships App!")