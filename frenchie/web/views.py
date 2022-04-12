from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from .forms import CreatePhotoForm, EditPhotoForm, DeletePhotoForm
from .models import *
import json

from ..helpers.form_control import FormControl


class HomePageView(ListView):
    model = AlbumPhoto
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photos = list(AlbumPhoto.objects.all())
        categories = list(Category.objects.all())

        context.update({
            'photos': photos,
            'categories': categories,
        })

        return context




class CreatePhotoView(CreateView, LoginRequiredMixin):
    form_class = CreatePhotoForm
    template_name = 'album/photo_create.html'
    success_url = reverse_lazy('home page')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPhotoView(UpdateView):
    form_class = EditPhotoForm
    template_name = 'album/photo_edit.html'
    success_url = reverse_lazy('home page')


class DeletePhotoView(DeleteView):
    form_class = DeletePhotoForm
    template_name = 'album/photo_delete.html'
    success_url = reverse_lazy('home page')


class Store(TemplateView):
    # if request.user.is_authenticated:
    #     customer = request.user
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    #     cart_items = order.get_cart_items
    # # else:
    # #     items = []
    # #     order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    # #     cart_items = order['get_cart_items']
    #
    # products = Product.objects.all()
    # context = {
    #     'products': products,
    #     # 'cart_items': cart_items,
    # }
    # return render(request, 'store/store.html', context)
    model = Product
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = None
        categories = list(Category.objects.all())
        category_id = self.request.GET.get('category')
        if category_id:
            products = Product.objects.filter(category=category_id)

        else:
            products = Product.objects.filter(category=1)

        context.update({
            'products': products,
            'categories': categories,
        })

        return context


