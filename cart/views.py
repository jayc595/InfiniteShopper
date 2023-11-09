from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


# Create your views here.

def _get_quote_id(request):
    quote = request.session.session_key
    if not quote:
        quote = request.session.create()
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


def remove_item_from_cart(request, product_id):
    cart = Cart.objects.get(quote_id=_get_quote_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.qty > 1:
        cart_item.qty -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def delete_item_from_cart(request, product_id):
    cart = Cart.objects.get(quote_id=_get_quote_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, qty=0, cart_items=None):
    context = _cart_items_context(request, total, qty, cart_items)
    return render(request, 'store/cart.html', context)


@login_required(login_url='login')
def checkout(request, total=0, qty=0, cart_items=None):
    context = _cart_items_context(request, total, qty, cart_items)
    return render(request, 'store/checkout.html', context)


def _cart_items_context(request, total=0, qty=0, cart_items=None):
    vat = 0
    grand_total = 0
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(quote_id=_get_quote_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total += (item.product.product_price * item.qty)
            qty += item.qty
        vat = (20 * total) / 100
        grand_total = total + vat
    except Exception as e:
        print(e)
            # ObjectDoesNotExist):
        # pass

    context = {
        'cart_items': cart_items,
        'total': total,
        'qty': qty,
        'vat': vat,
        'grand_total': grand_total,
    }
    return context
