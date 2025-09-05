from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import permission_required
from django.db.models import Count
from .models import Author, Book, BookInstance, Genre, Language, Publisher
from .forms import BookForm


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

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def librarian_dashboard(request):
    """
    View for the librarian dashboard. Requires 'can_add_book' permission.
    """
    return render(request, 'relationship_app/librarian_dashboard.html')
