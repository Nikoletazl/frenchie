from django.contrib import admin

from frenchie.web.models import AlbumPhoto, Product, Order, OrderItem


@admin.register(AlbumPhoto)
class PhotoAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass