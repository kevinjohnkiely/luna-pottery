from django.shortcuts import render
from products.models import Wishlist


def view_wishlist(request):
    """A view to render the wishlist page"""
    user = request.user

    wishlist_products = Wishlist.objects.filter(user=user)
    
    context = {
        'wishlist_products': wishlist_products
    }

    return render(request, 'wishlist/wishlist.html', context)
