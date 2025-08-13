"""
URL configuration for LibraryProject project.
"""
from django.contrib import admin
from django.urls import path, include
# Import RedirectView to handle the redirection
from django.views.generic.base import RedirectView

urlpatterns = [
    # This path will redirect the root URL ('/') to the 'bookshelf/' endpoint.
    path('', RedirectView.as_view(url='bookshelf/', permanent=True)),
    path('admin/', admin.site.urls),
    # The 'include' function tells Django to look for additional URL patterns
    # in the 'bookshelf.urls' module.
    path('bookshelf/', include('bookshelf.urls')),
]
