from django import forms

class RegistrationForm(forms.Form):
    """
    A form for user registration.

    Attributes:
        username (CharField): Field for entering the username.
        email (EmailField): Field for entering the email address.
        password (CharField): Field for entering the password.
    """
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
