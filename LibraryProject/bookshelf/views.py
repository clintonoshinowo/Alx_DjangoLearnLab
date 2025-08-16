# Import the HttpResponse class from the django.http module
from django.http import HttpResponse

# This is a simple view function. When a user visits the URL associated with
# this view, this function will run.
def hello_world(request):
    """
    A view that returns a simple 'Hello, world!' message.
    """
    # The view must return an HttpResponse object, or an exception.
    # We are returning a simple string as the response.
    return HttpResponse("Hello, world!")


