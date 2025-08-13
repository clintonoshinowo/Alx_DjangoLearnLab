# bookshelf/admin.py

from django.contrib import admin
from .models import Book # Import your Book model from the app's models.py

# Define the custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the display and functionality of the Book model
    in the Django admin interface.
    """
    # list_display: Controls which fields are displayed as columns on the change list page.
    list_display = ('title', 'author', 'publication_year')

    # list_filter: Adds filters to the right sidebar of the change list page,
    # allowing users to filter by specific field values.
    list_filter = ('publication_year', 'author')

    # search_fields: Enables a search box on the change list page,
    # allowing users to search across the specified fields.
    search_fields = ('title__icontains', 'author__icontains')

# Register the Book model with its custom admin class
admin.site.register(Book, BookAdmin)
# bookshelf/admin.py

from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
