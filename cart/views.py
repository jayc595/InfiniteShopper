from django.shortcuts import render, redirect
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse


# Create your views here.

def _get_quote_id(request):
    quote = request.session.session_key
    if not quote:
        quote = request.session.create
    return quote


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(quote_id=_get_quote_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            quote_id=_get_quote_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.qty += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
            qty=1,
        )
    cart_item.save()
    # return HttpResponse(cart_item.product)
    # exit()
    return redirect('cart')


def cart(request):
    return render(request, 'store/cart.html')
