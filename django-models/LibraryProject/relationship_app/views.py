from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import permission_required
from django.db.models import Count
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book, BookInstance, Genre, Language, Publisher
from .forms import BookForm


# --- Generic Class-Based Views for Lists and Details ---
# These are the views that were missing and caused the error.

class BookListView(generic.ListView):
    """Generic class-based list view for books."""
    model = Book
    paginate_by = 10

class BookDetailView(generic.DetailView):
    """Generic class-based detail view for a book."""
    model = Book

class AuthorListView(generic.ListView):
    """Generic class-based list view for authors."""
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    """Generic class-based detail view for an author."""
    model = Author

# --- New Views for Book Management ---
# These views are Django's generic views for handling forms.
class BookCreateView(CreateView):
    """Generic class-based view to create a new book."""
    model = Book
    fields = ['title', 'author', 'genre', 'publication_date']
    success_url = reverse_lazy('books')

class BookUpdateView(UpdateView):
    """Generic class-based view to update an existing book."""
    model = Book
    fields = ['title', 'author', 'genre', 'publication_date']
    success_url = reverse_lazy('books')

class BookDeleteView(DeleteView):
    """Generic class-based view to delete an existing book."""
    model = Book
    success_url = reverse_lazy('books')

# --- Existing Function-Based Views ---
# All the views you provided in the last message are here.

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
