from django.urls import path
from .import views

urlpatterns = [
    path('', views.view_wishlist, name='wishlist'),
    path('wishlist/<int:product_id>',
         views.remove_from_wishlist, name='remove_from_wishlist'),
]