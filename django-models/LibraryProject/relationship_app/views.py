# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth import login
from .models import Library
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Main index page view, currently a placeholder.
def index(request):
    return render(request, "relationship_app/index.html")

# View to display a single library's details.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# View to list all books (placeholder).
def list_books(request):
    return render(request, "relationship_app/list_books.html")

# New view for user registration.
def register(request):
    # If the request is a POST, the form has been submitted.
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the new user and automatically log them in.
            user = form.save()
            login(request, user)
            # Redirect to the home page or a success page.
            return redirect("relationship_app:index")
    else:
        # If the request is a GET, display an empty registration form.
        form = UserRegistrationForm()
    
    # Render the registration page with the form.
    return render(request, "relationship_app/register.html", {"form": form})
