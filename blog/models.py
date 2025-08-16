# blog/models.py

from django.db import models
from django.contrib.auth.models import User

# The Post model for a blog post.
class Post(models.Model):
    """
    A model to represent a blog post with a title, content,
    publication date, and author.
    """
    # The title of the blog post.
    title = models.CharField(max_length=200)

    # The main body content of the post.
    content = models.TextField()

    # The date and time the post was published. This field
    # is automatically set to the current time when the object is created.
    published_date = models.DateTimeField(auto_now_add=True)

    # A ForeignKey to the Django's built-in User model.
    # This creates a one-to-many relationship, meaning a user can have
    # many posts, but each post has only one author.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the post.
        """
        return self.title

# Create your models here.
