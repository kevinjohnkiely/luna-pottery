from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """A view to render the list of products page, including sorting & searching"""

    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'products/products.html', context)


def product_single(request, product_id):
    """A view to render a single page showing the individual product details"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_single.html', context)
