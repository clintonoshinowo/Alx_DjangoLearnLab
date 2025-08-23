from django.urls import path
from .views import list_all_books, LibraryDetailView
from . import views
# Define the URL patterns for the relationship_app
urlpatterns = [
    # Path for the function-based view to list all books
    # The name 'list_books' is used for URL reversal in templates
    path('books/', list_all_books, name='list_books'),

    # Path for the class-based view to show a single library's details
    # <int:pk> is a dynamic path converter that matches an integer primary key
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # This path matches the root of the app URL (e.g., http://127.0.0.1:8000/)
    # and calls the 'list_books' function in views.py
    path('', views.list_all_books, name='list_books'),
]
