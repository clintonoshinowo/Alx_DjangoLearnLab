# django-models/urls.py
from django.urls import path
from . import views

# Set the app_name for URL namespacing.
app_name = 'django-models'

urlpatterns = [
    # URL pattern for the 'Admin' view
    path('admin_view/', views.admin_view, name='admin_view'),

    # URL pattern for the 'Librarian' view
    path('librarian_view/', views.librarian_view, name='librarian_view'),

    # URL pattern for the 'Member' view
    path('member_view/', views.member_view, name='member_view'),
]
