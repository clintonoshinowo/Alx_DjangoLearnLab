# advanced_features_and_security/models.py

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model.
    It overrides the default user and superuser creation methods
    to ensure the new fields are handled correctly.
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a regular user with the given email and password.
        The email is set as the username to ensure uniqueness.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        # Ensure superusers have the necessary permissions
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
            
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    """
    A custom user model that extends Django's AbstractUser.
    We are replacing the default username field with email for login,
    and adding a date of birth and a profile photo.
    """
    # Overriding the default username field to use email for authentication
    username = None
    email = models.EmailField(_('email address'), unique=True)
    
    # Adding custom fields
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    # Use the custom manager for this model
    objects = CustomUserManager()

    # Set the email field as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # No extra required fields at creation for superuser

    def __str__(self):
        return self.email

# Create your models here.
