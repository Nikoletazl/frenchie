from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from frenchie.auth_app.forms import RegisterForm, LoginForm


class UserRegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
