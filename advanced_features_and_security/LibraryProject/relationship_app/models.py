# relationship_app/models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Note: assuming authors.py and publishers.py are separate modules with
# Author and Publisher models defined. If they are in this file,
# the imports are not needed and the classes should be moved.
# from .authors import Author
# from .publishers import Publisher

# Define the user roles as choices
ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    """
    A model to hold additional information for a user, like their role.
    It has a OneToOne relationship with Django's built-in User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        """String for representing the UserProfile object."""
        return f"{self.user.username}'s Profile - {self.role}"

# Signal to automatically create a UserProfile when a new User is created.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    This signal function listens for the 'post_save' event on the User model.
    If a new user is created ('created' is True), it automatically creates
    a corresponding UserProfile instance.
    """
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    This signal function listens for the 'post_save' event on the User model
    and ensures the UserProfile is saved whenever the User is saved.
    """
    instance.userprofile.save()

class Author(models.Model):
    """Represents a book author."""
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)

    def __str__(self):
        """String for representing the Author object."""
        return self.name

class Publisher(models.Model):
    """Represents a book publisher."""
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """String for representing the Publisher object."""
        return self.name

class Book(models.Model):
    """
    Represents a book in the library.
    It has ForeignKey relationships to Author and Publisher, and includes custom permissions.
    """
    title = models.CharField(max_length=200)
    publication_date = models.DateField(blank=True, null=True) 
    
    # ForeignKey relationships
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True, null=True)

    # Corrected ISBN field definition, all on one line or in one block.
    # The null=True argument is necessary to fix the migration issue.
    isbn = models.CharField(
        'ISBN',
        max_length=13,
        unique=True,
        null=True, # This is the key change to solve the error
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>'
    )
    
    # Fields from the user's provided code
    summary = models.TextField(
        max_length=1000,
        help_text="Enter a brief description of the book"
    )

    class Meta:
        # Define the custom permissions for this model.
        permissions = [
            ("can_add_book", "Can add a book entry"),
            ("can_change_book", "Can change a book entry"),
            ("can_delete_book", "Can delete a book entry"),
        ]

    def __str__(self):
        """String for representing the Book object."""
        return self.title

class Library(models.Model):
    """Represents a library that can hold multiple books."""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        """String for representing the Library object."""
        return self.name

class Librarian(models.Model):
    """Represents a librarian associated with a specific library."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        """String for representing the Librarian object."""
        return self.name
