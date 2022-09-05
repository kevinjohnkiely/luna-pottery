from django.shortcuts import render, redirect, reverse, HttpResponse
from products.models import Product
from django.contrib import messages


def view_cart(request):
    """A view to render the cart contents page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of selected item to the shopping cart """

    product = Product.objects.get(pk=item_id)

    qty = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += qty
    else:
        cart[item_id] = qty
        messages.error(request, f'You added {product.name} to the cart')

    request.session['cart'] = cart
    
    return redirect(redirect_url)


def alter_cart(request, item_id):
    """ Adjust quantity of selected item to the shopping cart """
    qty = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if qty > 0:
        cart[item_id] = qty
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove an item from the shopping cart """

    try:
        cart = request.session.get('cart', {})
        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)
        
    except Exception as e:
        return HttpResponse(status=500)