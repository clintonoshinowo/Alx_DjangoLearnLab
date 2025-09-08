from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

# Helper functions for role checks
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin, login_url='/access-denied/')
def admin_view(request):
    """
    View accessible only by users with the 'Admin' role.
    """
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/access-denied/')
def librarian_view(request):
    """
    View accessible only by users with the 'Librarian' role.
    """
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/access-denied/')
def member_view(request):
    """
    View accessible only by users with the 'Member' role.
    """
    return render(request, 'member_view.html')

def access_denied(request):
    """
    A simple view for access denied page.
    """
    return render(request, 'access_denied.html')
