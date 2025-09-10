from django import forms

class ExampleForm(forms.Form):
    """
    This form defines a simple text input field for a secure example.
    Django forms provide built-in validation and cleaning of input data,
    which is a key security measure against various attacks, including XSS.
    """
    user_input = forms.CharField(label="Enter something", max_length=100)
