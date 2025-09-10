from django.urls import path
from . import views

urlpatterns = [
    # General app views
    path('', views.index, name='index'),

    # Author and Book list and detail views (Class-based)
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

    # Book management views (Function-based)
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Librarian dashboard
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]
