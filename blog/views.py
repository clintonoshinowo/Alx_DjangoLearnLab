from django.shortcuts import render

def index(request):
    """
    A simple view to render the main blog index page.
    """
    return render(request, 'blog/index.html')

# Create your views here.
