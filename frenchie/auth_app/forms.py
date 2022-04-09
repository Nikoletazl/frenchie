from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter an username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter an email',
                }
            ),
            'password1': forms.TextInput(
                attrs={
                    'placeholder': 'Enter a valid password',
                }
            ),
            'password2': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the same password',
                }
            ),
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter you username',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'placeholder': 'Enter you password',
                }
            ),
        }


class UserResetPasswordForm(PasswordResetForm):
    pass