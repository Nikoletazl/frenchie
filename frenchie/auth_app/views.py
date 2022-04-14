from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView, ListView, UpdateView

from frenchie.auth_app.forms import CreateProfileForm, EditProfileForm
from frenchie.auth_app.models import Customer, FrenchieUser
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


class Profile(DetailView):
    model = Customer
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'


class EditProfileView(UpdateView):
    model = Customer
    form_class = EditProfileForm
    template_name = 'accounts/edit.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        if self.success_url:
            return self.success_url


    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)



