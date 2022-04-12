from django.shortcuts import render
from django.http import JsonResponse
from django.template import response
import datetime

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from .forms import CreatePhotoForm, EditPhotoForm, DeletePhotoForm
from .models import *
import json


class HomePageView(ListView):
    model = AlbumPhoto
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(AlbumPhoto.objects.all())

        context.update({
            'photos': photos,
        })

        return context


class CreatePhotoView(CreateView):
    form_class = CreatePhotoForm
    template_name = 'album/photo_create.html'
    success_url = reverse_lazy('home page')


class EditPhotoView(UpdateView):
    form_class = EditPhotoForm
    template_name = 'album/photo_edit.html'
    success_url = reverse_lazy('home page')


class DeletePhotoView(DeleteView):
    form_class = DeletePhotoForm
    template_name = 'album/photo_delete.html'
    success_url = reverse_lazy('home page')


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cart_items = order['get_cart_items']

    products = Product.objects.all()
    context = {
        'products': products,
        'cart_items': cart_items,
    }
    return render(request, 'store/store.html', context)
