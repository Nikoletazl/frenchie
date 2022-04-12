from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home page"),

    path('store/', views.store, name="store"),

    path('create/photo/', views.CreatePhotoView.as_view(), name="create photo"),
    path('edit/photo/<int:pk>', views.EditPhotoView.as_view(), name="edit photo"),
    path('delete/photo/<int:pk>', views.DeletePhotoView.as_view(), name="delete photo"),
]
