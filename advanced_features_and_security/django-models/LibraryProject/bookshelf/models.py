from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def _str_(self):
        return self.username
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    title = models.IntegerField()

    def__str__(self):
        return self.title