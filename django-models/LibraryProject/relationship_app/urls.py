# Import the path function and the views from the current directory
from django.urls import path
from . import views

# Define the URL patterns for this app
urlpatterns = [
    # This maps the root of the app to the 'index' view.
    path('', views.index, name='index'),
]
