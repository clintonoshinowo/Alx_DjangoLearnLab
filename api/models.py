from django.db import models

# Model to represent an Author.
# This is a simple model with just a name field.
class Author(models.Model):
    """
    Represents an author of books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model to represent a Book.
# It has a foreign key to Author, establishing a one-to-many relationship.
class Book(models.Model):
    """
    Represents a book written by an author.
    The 'author' field is a ForeignKey, creating a one-to-many relationship
    where one Author can have many Books. The 'related_name' attribute allows
    us to access the list of a book's books from the author instance
    (e.g., author.books.all()).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books' # This allows access to books from an Author object
    )

    def __str__(self):
        return f"{self.title} by {self.author.name}"

# Create your models here.
