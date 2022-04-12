from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('frenchie.auth_app.urls')),
    path('cart/', include('frenchie.cart.urls')),
    path('', include('frenchie.web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

