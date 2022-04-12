from django.urls import path

from frenchie.cart import views

urlpatterns = (
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('process_order/', views.process_order, name="process order"),
    path('update_item/', views.updateItem, name="update item"),
)