# Import the path function and the views from the current directory
from django.urls import path
from . import views

# Define the URL patterns for this app
urlpatterns = [
    # This maps the root of the app to the 'index' view.
    path('', views.index, name='index'),
    # Path for the librarian-only dashboard
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('book/add/', views.BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/edit/', views.BookUpdateView.as_view(), name='book_edit'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    
    # Add other existing URL patterns here
    # For example:
    # path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
