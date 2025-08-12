"""
URL configuration for advanced_api_project project.
"""
from django.contrib import admin
from django.urls import path, include # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URLs from your 'api' app.
    # This will route all requests starting with 'api/' to your app's URLs.
    path('api/', include('api.urls')),
]
