import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Define the choices for the user's role
# Using a tuple of tuples is the recommended Django way to define choices
# The first value is the actual value stored in the database, and the second
# value is the human-readable name displayed in the Django admin site.
LIBRARIAN = 'librarian'
MEMBER = 'member'
USER_ROLES = (
    (LIBRARIAN, 'Librarian'),
    (MEMBER, 'Member'),
)

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)."""
        return self.name

class Genre(models.Model):
    """Model representing a book genre (e.g. Science Fiction, Fantasy)."""
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Publisher(models.Model):
    """Model representing a book publisher."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13, unique=True,
                               help_text='13 Character ISBN number')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    publication_date = models.DateField(null=True, blank=True)

    # Added the Meta class with permissions here
    class Meta:
        permissions = (
            ('can_manage_books', 'Can add, edit, or delete books'),
        )

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

class UserProfile(models.Model):
    """
    Extends the Django User model with a one-to-one relationship
    and includes a role field to identify user types.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=USER_ROLES, default=MEMBER)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
