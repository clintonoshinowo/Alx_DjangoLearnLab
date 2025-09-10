# advanced_features_and_security/another_app/models.py
# This is an example to show how to update other models

from django.db import models
from django.conf import settings

class Post(models.Model):
    """
    An example model that has a foreign key to the user model.
    """
    # Use settings.AUTH_USER_MODEL to reference your custom user model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
 
