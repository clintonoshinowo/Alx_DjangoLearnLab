# Import the path function and the views from the current directory
from django.urls import path
from . import views

# Define the URL patterns for this app
urlpatterns = [
    # This maps the root of the app to the 'index' view.
    path('', views.index, name='index'),
    # Path for the librarian-only dashboard
    path('librarian/', views.librarian_dashboard, name='librarian_dashboard'),
    
    # Add other existing URL patterns here
    # For example:
    # path('profile/<str:username>/', views.user_profile, name='user_profile'),
]
