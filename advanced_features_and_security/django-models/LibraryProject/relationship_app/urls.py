# LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views
from . import views  # Corrected import statement
from .views import AddBookView

app_name = "relationship_app"

urlpatterns = [
     # ... other URL patterns ...
    path('librarian/', views.librarian_view, name='librarian_view'),
    # Path for the index page.
    path("", views.index, name="index"),
    
    # Path for user registration. Uses the explicit 'views.register' format.
    path("register/", views.register, name="register"),

    # Path for user login.
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # Path for user logout.
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    # Path for a view that requires the user to have 'librarian' permissions
    path('librarian/', views.librarian_view, name='librarian_view'),
    # Paths for managing books, secured by specific permissions
    path('books/', views.list_books, name='list_books'),
    path('book/change/<int:pk>/', views.change_book, name='change_book'),
    path('book/delete/<int:pk>/', views.delete_book, name='delete_book'),
    # This URL pattern correctly maps the '/book/add/' path to the AddBookView class.
    path('book/add/', AddBookView.as_view(), name='add_book'),
]
