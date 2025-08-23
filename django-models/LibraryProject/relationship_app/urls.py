# LibraryProject/relationship_app/urls.py

from django.urls import path
# Import built-in views for login and logout
from django.contrib.auth.views import LoginView, LogoutView
# Import your custom register view and other existing views
from .views import index, LibraryDetailView, list_books, register

app_name = "relationship_app"

urlpatterns = [
    # Existing URL patterns
    path("", index, name="index"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("books/", list_books, name="list_books"),

    # New URL patterns for authentication
    # The login view handles user authentication. We specify the template name.
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    
    # The logout view logs the user out. It redirects to a URL defined in settings.py.
    path("logout/", LogoutView.as_view(), name="logout"),

    # The registration view uses your custom view function.
    path("register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]
