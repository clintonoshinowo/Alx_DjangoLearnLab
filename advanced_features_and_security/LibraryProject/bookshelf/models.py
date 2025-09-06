from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    # Add an email field, which is often used for user accounts
    email = models.EmailField(unique=True, null=True, blank=True)

    # You must set the objects manager for Django to recognize your custom manager.
    objects = CustomUserManager()

    # The username field is already provided by AbstractUser. You can keep it or remove it.
    # To use `email` as the primary login field, you need to set it as the USERNAME_FIELD
    USERNAME_FIELD = "email"

    # Define a list of fields that will be prompted for when a user is created with `createsuperuser`
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
