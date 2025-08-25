# LibraryProject/relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login # NEW IMPORT
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# This is a custom decorator that acts as a "bouncer."
# It checks if the logged-in user belongs to the specified group.
def group_required(group_name):
    """
    Decorator to check if the user is a member of the given group.
    """
    def decorator(view_func):
        @login_required(login_url='/admin/login/') # First, ensure the user is logged in
        def wrapper(request, *args, **kwargs):
            try:
                # Check if the user's groups contain the required group name.
                if request.user.groups.filter(name=group_name).exists():
                    # If they are in the group, let them see the view.
                    return view_func(request, *args, **kwargs)
                else:
                    # If not, redirect them to the home page or another designated page.
                    return redirect('/')
            except Exception as e:
                # Handle potential errors gracefully and redirect.
                print(f"An error occurred: {e}")
                return redirect('/')
        return wrapper
    return decorator

# This is the view for the exclusive 'Librarian' page.
# The decorator above ensures only authorized users can access it.
@group_required('Librarians')
def librarian_dashboard(request):
    """
    Renders the dashboard page specifically for librarians.
    """
    # This view simply renders the HTML template.
    return render(request, 'librarian_dashboard.html')


# myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... other url patterns
    # This URL pattern maps '/librarian_dashboard/' to our new view.
    path('librarian_dashboard/', views.librarian_dashboard, name='librarian_dashboard'),
]


# myproject/templates/librarian_dashboard.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Librarian Dashboard</title>
    <style>
        body {
            font-family: sans-serif;
            text-align: center;
            padding-top: 50px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, Librarian!</h1>
        <p>This is your exclusive dashboard. Access to this page is restricted to users in the 'Librarians' group.</p>
        <p>You can now add content and functionality that only librarians should see.</p>
        <a href="/admin/logout/">Logout</a>
    </div>
</body>
</html>
rom django.contrib.auth.decorators import user_passes_test

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
