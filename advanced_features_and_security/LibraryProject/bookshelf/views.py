from django.shortcuts import render
from .models import Book
from django.http import HttpResponseBadRequest
import re
from .forms import ExampleForm  # The missing import, now added.

def book_list(request):
    """
    Renders a list of books.
    This view demonstrates a simple, safe use of the Django ORM.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def search_books(request):
    """
    A view to demonstrate secure handling of user input to prevent SQL injection.
    It uses Django's ORM, which handles parameterization automatically.
    """
    query = request.GET.get('q', '')
    if query:
        # The Django ORM safely parameterizes the query, preventing SQL injection.
        sanitized_query = query.strip()
        
        if not re.match(r"^[a-zA-Z0-9\s]+$", sanitized_query):
            return HttpResponseBadRequest("Invalid search query. Please use only alphanumeric characters and spaces.")

        books = Book.objects.filter(title__icontains=sanitized_query)
    else:
        books = Book.objects.all()
    
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

def form_example(request):
    """
    A view that securely handles form submissions using Django's Form classes.
    """
    message = None
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request.
        form = ExampleForm(request.POST)
        
        # Check if the form is valid. This automatically runs the defined
        # validation rules, such as max_length, and provides a clean data dictionary.
        if form.is_valid():
            # Data is now sanitized and ready to use.
            user_input = form.cleaned_data['user_input']
            message = f"Form submitted successfully! Your input was: '{user_input}'"
        else:
            # If the form is not valid, the form object contains error messages.
            message = "Form submission failed. Please check the input."
    else:
        # If it's a GET request, create an empty form instance.
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form, 'message': message})
