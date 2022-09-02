from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    cart_total = 0
    cart_items_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        cart_total += quantity * product.price
        cart_items_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if cart_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = cart_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE)
        free_delivery_amount_remaining = settings.FREE_DELIVERY_THRESHOLD - cart_total
    else:
        delivery = 0
        free_delivery_amount_remaining = 0

    grand_total = delivery + cart_total

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_items_count': cart_items_count,
        'delivery': delivery,
        'free_delivery_amount_remaining': free_delivery_amount_remaining,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total
    }

    return context