# bookshelf/views.py

from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    A simple view that returns an HTTP response with a "Hello, world!" message.
    """
    return HttpResponse("Hello, world! This is the bookshelf app.")

def profile(request):
    """
    A placeholder view for the user profile page.
    """
    return HttpResponse("This is the user profile page.")
