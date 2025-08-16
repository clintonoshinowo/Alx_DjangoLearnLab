# bookshelf/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # This path matches the root URL of the app (e.g., /bookshelf/).
    # It tells Django to run the `hello_world` view when this URL is accessed.
    path('', views.hello_world, name='hello_world'),
    path('profile/', views.profile, name='profile'),
]
