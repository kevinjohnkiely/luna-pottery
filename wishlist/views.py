from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Wishlist
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """A view to render the wishlist page"""
    user = request.user
    wishlist_products = Wishlist.objects.filter(user=user)
    
    context = {
        'wishlist_products': wishlist_products
    }

    return render(request, 'wishlist/wishlist.html', context)


def remove_from_wishlist(request, product_id):
    """A method to remove the wishlisted product"""
    user = request.user
    wishlist_products = Wishlist.objects.filter(user=user)

    wishlist_to_delete = get_object_or_404(wishlist_products, id=product_id)
    wishlist_to_delete.delete()

    return redirect(reverse('wishlist'))
