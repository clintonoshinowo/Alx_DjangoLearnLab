# LibraryProject/relationship_app/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import built-in views
from .views import index, register  # Import your custom views

app_name = "relationship_app"

urlpatterns = [
    # Path for the index page.
    path("", index, name="index"),
    
    # Path for user registration. It uses your custom 'register' view function.
    path("register/", register, name="register"),

    # Path for user login. It uses Django's built-in LoginView and specifies a template.
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),

    # Path for user logout. It uses Django's built-in LogoutView and specifies a template.
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
