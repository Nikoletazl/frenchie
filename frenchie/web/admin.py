from django.contrib import admin

from frenchie.web.models import AlbumPhoto, Product, Category


@admin.register(AlbumPhoto)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass