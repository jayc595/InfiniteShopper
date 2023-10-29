from cart.models import Cart,CartItem
from cart.views import _get_quote_id
from django.core.exceptions import ObjectDoesNotExist


def get_cart_item_total(request):
    try:
        cart = Cart.objects.get(quote_id=_get_quote_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        item_total = cart_items.count()
    except Cart.DoesNotExist:
        item_total = 0
    return dict(item_total=item_total)