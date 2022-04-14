from django.urls import path

from . import views
from ..cart.views import updateItem, process_order

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home page"),

    path('store/', views.Store.as_view(), name="store"),
    path('update_item/', updateItem, name="update item"),
    path('process_order/', process_order, name="process order"),

    path('create/photo/', views.CreatePhotoView.as_view(), name="create photo"),
    path('edit/photo/<int:pk>', views.EditPhotoView.as_view(), name="edit photo"),
    path('delete/photo/<int:pk>', views.DeletePhotoView.as_view(), name="delete photo"),
]
