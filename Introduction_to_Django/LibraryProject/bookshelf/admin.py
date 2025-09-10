from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters by author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality on these fields
    search_fields = ('title', 'author')
# Register your models here.
