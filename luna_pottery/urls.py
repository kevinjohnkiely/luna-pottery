from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('welcome.urls')),
    path('products/', include('products.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'luna_pottery.views.handler404'
