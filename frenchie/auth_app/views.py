from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from frenchie.auth_app.forms import CreateProfileForm
from frenchie.helpers.form_control import FormControl
from frenchie.web.models import Product


class UserRegistrationView(CreateView):
    form_class = CreateProfileForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home page')

    def get_success_url(self):
        if self.success_url:
            return self.success_url


class ProductCreateView(UserPassesTestMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'admin/product_create.html'
    success_url = reverse_lazy('store')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff



