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

        context.update({
            'photos': photos,
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
    model = Product
    template_name = 'store/store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()


        context.update({
            'products': products,

        })

        return context



