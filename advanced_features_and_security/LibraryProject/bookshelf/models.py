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
    # This field is set to 'email' in a custom user model for login purposes.
    USERNAME_FIELD = "email"

    # Django will prompt for these fields when a superuser is created.
    REQUIRED_FIELDS = []

    # The email field is the unique identifier for this user.
    email = models.EmailField(unique=True)

    # You must set the objects manager for Django to recognize your custom manager.
    objects = CustomUserManager()

    # Additional fields for the user profile
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.email

class Book(models.Model):
    """
    Represents a book in the library management system.
    This model includes custom permissions to control user actions.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    class Meta:
        # Define custom permissions for the Book model.
        # These permissions will be used to create user groups with specific access levels.
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create new books"),
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete books"),
        ]

    def __str__(self):
        return self.title
