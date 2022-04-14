from django.urls import path

from frenchie.auth_app.views import UserRegistrationView, UserLoginView, ProductCreateView, Profile, EditProfileView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('profile/<int:pk>/', Profile.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', EditProfileView.as_view(), name='profile edit'),

    path('add/product/', ProductCreateView.as_view(), name='add product'),
)