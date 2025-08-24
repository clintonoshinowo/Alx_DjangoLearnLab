# LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views
from . import views  # Corrected import statement

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
]
