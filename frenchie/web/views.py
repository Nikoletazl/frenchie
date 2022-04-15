from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from .forms import CreatePhotoForm, EditPhotoForm, DeletePhotoForm
from .models import *
import json


class HomePageView(ListView):
    model = AlbumPhoto
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(AlbumPhoto.objects.all())

        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cart_items = order.get_cart_items

        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']

        products = Product.objects.all()
        request_user = self.request.user

        context.update({
            'photos': photos,
            'products': products,
            'cart_items': cart_items,
            'request_user': request_user,
        })

        return context


class CreatePhotoView(CreateView, LoginRequiredMixin):
    model = AlbumPhoto
    form_class = CreatePhotoForm
    template_name = 'album/photo_create.html'
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs


class EditPhotoView(UpdateView, LoginRequiredMixin):
    model = AlbumPhoto
    form_class = EditPhotoForm
    template_name = 'album/photo_edit.html'
    success_url = reverse_lazy('home page')
    context_object_name = 'photo'

    def get_success_url(self):
        if self.success_url:
            return self.success_url

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)


class DeletePhotoView(DeleteView, LoginRequiredMixin):
    model = AlbumPhoto
    form_class = DeletePhotoForm
    template_name = 'album/photo_delete.html'
    success_url = reverse_lazy('home page')
    context_object_name = 'photo'


class Store(TemplateView):
    model = Product
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            customer = self.request.user
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cart_items = order.get_cart_items

        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']


        products = Product.objects.all()
        context.update({
            'products': products,
            'cart_items': cart_items,
        })

        return context
