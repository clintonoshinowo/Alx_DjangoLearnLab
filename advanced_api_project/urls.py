# advanced_api_project/urls.py

from django.contrib import admin
from django.urls import path, include
# Import RedirectView to handle the redirection
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    # New line: Redirect the root URL (http://127.0.0.1:8000/) to the API root.
    # The 'permanent=True' argument indicates this is a permanent redirect.
    path('', RedirectView.as_view(url='api/', permanent=True)),
]
