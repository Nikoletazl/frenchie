from django.urls import path

from frenchie.auth_app.views import UserRegistrationView, UserLoginView, ProductCreateView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('add/product/', ProductCreateView.as_view(), name='add product'),
)