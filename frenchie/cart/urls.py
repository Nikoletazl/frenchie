from django.urls import path

from frenchie.cart import views

urlpatterns = (
    path('', views.Cart.as_view(), name="cart"),
    path('checkout/', views.Checkout.as_view(), name="checkout"),


)