# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login # NEW IMPORT
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# View for the index page.
def index(request):
    """The home page for the relationship_app."""
    return render(request, "relationship_app/index.html")

# View for user registration.
def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to the home page.
            login(request, new_user) # NEW LINE
            return redirect(reverse_lazy("relationship_app:index"))

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "relationship_app/register.html", context)
