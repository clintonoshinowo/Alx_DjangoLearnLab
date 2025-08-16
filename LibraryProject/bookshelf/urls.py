# Import the path function and your views from the current app
from django.urls import path
from . import views

# This is a list of URL patterns for the 'bookshelf' app.
# The 'name' argument gives a name to the URL, which is helpful for
# referring to it in templates or other parts of your code.
urlpatterns = [
    # The first argument, '', means this will match the root of the app's URL.
    # The second argument tells Django to use the 'hello_world' function
    # from the views.py file.
    path('', views.hello_world, name='hello_world'),
]

