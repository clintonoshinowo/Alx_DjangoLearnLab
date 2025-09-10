from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Define the user role choices
ROLES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
)

class UserProfile(models.Model):
    """
    Extends the built-in User model with a one-to-one relationship
    to include a user role.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile - {self.role}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Django signal to automatically create a UserProfile
    when a new User instance is created.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # If the user already exists, save the profile to update it
    instance.userprofile.save()
