# relationship_app/models.py

from django.db import models

# A model with a ManyToMany relationship to itself is used for more complex scenarios,
# but for this exercise we will stick with the prompt.

class Author(models.Model):
    """
    Represents an author. A single author can have many books.
    This model will be the 'one' in the one-to-many (ForeignKey) relationship.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book. A book has one author.
    This model has a ForeignKey to the Author model.
    """
    title = models.CharField(max_length=200)
    # ForeignKey creates a one-to-many relationship. A book has ONE author, but an
    # author can have MANY books. on_delete=models.CASCADE means if the Author is
    # deleted, all their books will also be deleted.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.title}" by {self.author.name}'

class Library(models.Model):
    """
    Represents a library. A library can have many books, and a book can be in
    many libraries.
    This model has a ManyToManyField to the Book model.
    """
    name = models.CharField(max_length=100)
    # ManyToManyField creates a many-to-many relationship. A Library can have
    # many Books, and a Book can belong to many Libraries.
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    """
    Represents a librarian. A librarian is uniquely associated with one library.
    This model has a OneToOneField to the Library model.
    """
    name = models.CharField(max_length=100)
    # OneToOneField creates a one-to-one relationship. A Librarian can be linked
    # to only ONE Library, and a Library can have only ONE Librarian.
    # on_delete=models.CASCADE ensures that if a Library is deleted, its
    # associated Librarian record is also deleted.
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
