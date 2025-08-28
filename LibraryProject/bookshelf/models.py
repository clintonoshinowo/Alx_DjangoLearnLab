# bookshelf/models.py

from django.db import models
from django.conf import settings

class Author(models.Model):
    """
    Represents an author of a book.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    class Meta:
        # A simple check to ensure no duplicate authors are created.
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    """
    Represents a publisher of books.
    """
    name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book in the library.
    It links to Authors, a Publisher, and the user who added it.
    """
    title = models.CharField(max_length=200)
    # The 'on_delete' ensures that if an author is deleted, all their books remain.
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    publication_date = models.DateField(null=True, blank=True)

    # This is the crucial part that links the book to your custom user.
    # It correctly references your CustomUser model via the settings.
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

