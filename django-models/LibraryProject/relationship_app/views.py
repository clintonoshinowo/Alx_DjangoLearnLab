# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login # NEW IMPORT
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import user_passes_test

def is_librarian(user):
    """
    Checks if the user belongs to the 'Librarians' group.
    """
    return user.groups.filter(name='Librarians').exists()

@user_passes_test(is_librarian)
def librarian_view(request):
    """
    A view accessible only to users who are in the 'Librarians' group.
    """
    return render(request, 'relationship_app/librarian_view.html', {})
# --- Test functions for user roles ---
# These functions will be used by the @user_passes_test decorator.
def is_admin(user):
    """Checks if the user's role is 'Admin'."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Checks if the user's role is 'Librarian'."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Checks if the user's role is 'Member'."""
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# --- Views restricted by role ---
@user_passes_test(is_admin)
def admin_view(request):
    """View for users with the 'Admin' role."""
    return render(request, 'django-models/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    """View for users with the 'Librarian' role."""
    return render(request, 'django-models/librarian_view.html')

# We can use @login_required for the member view since it's the default role,
# but using @user_passes_test with our function is a good practice for consistency.
@user_passes_test(is_member)
def member_view(request):
    """View for users with the 'Member' role."""
    return render(request, 'django-models/member_view.html')

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
