from django.urls import path
from .import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_single, name='product_single'),
    # path('rate_product/<int:product_id>',
    #      views.rate_product, name='rate_product'),
]
