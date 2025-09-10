from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for the Book model.
    This form will automatically create input fields for the 'title' and 'publication_date'
    fields of the Book model.
    """
    class Meta:
        # The 'model' attribute tells the form which model it is associated with.
        model = Book
        # The 'fields' attribute specifies which fields from the model
        # should be included in the form.
        fields = ['title', 'publication_date']


# The UserRegistrationForm inherits from Django's built-in UserCreationForm.
# This form handles creating a new user and validating the password.
class UserRegistrationForm(UserCreationForm):
    # We are not adding any extra fields for this example, but you could add
    # custom fields here if needed.
    pass
