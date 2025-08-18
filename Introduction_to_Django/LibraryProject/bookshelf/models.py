from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.Charfield(max_length=200)
    author = models.Charfield(max_length=100)
    title = models.IntegerField()

    def__str__(self):
        return self.title