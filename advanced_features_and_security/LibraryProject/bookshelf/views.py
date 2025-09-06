from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden

from .models import Book

def index(request):
    """
    The main landing page, which is accessible to all users.
    """
    return render(request, 'base_template.html', {'message': 'Welcome to the Library Management System!'})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of all books. Access is restricted to users with the 'can_view' permission.
    """
    # Fetch all book objects from the database
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    View to handle the creation of a new book. Requires the 'can_create' permission.
    """
    if request.method == 'POST':
        # Add logic here to save the new book data from the form
        return redirect('book_list')
    return render(request, 'book_form.html', {'form_title': 'Create New Book'})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    View to handle editing an existing book. Requires the 'can_edit' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Add logic here to save the edited book data from the form
        return redirect('book_list')
    return render(request, 'book_form.html', {'form_title': 'Edit Book'})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    View to delete a book. Requires the 'can_delete' permission.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

# Create your views here.
