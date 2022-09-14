from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_single, name='product_single'),
    path('rating/<int:product_id>',
         views.add_rating, name='add_rating'),
    path('wishlist/<int:product_id>',
         views.add_to_wishlist, name='add_to_wishlist'),
]
