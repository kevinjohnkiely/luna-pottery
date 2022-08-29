from django.shortcuts import render
from .models import Product


def all_products(request):
    """A view to render the list of products page, including sorting & searching"""

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)
