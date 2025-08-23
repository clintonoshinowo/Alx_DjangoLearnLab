from django.contrib.auth.forms import UserCreationForm

# The UserRegistrationForm inherits from Django's built-in UserCreationForm.
# This form handles creating a new user and validating the password.
class UserRegistrationForm(UserCreationForm):
    # We are not adding any extra fields for this example, but you could add
    # custom fields here if needed.
    pass
