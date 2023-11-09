from cart.models import Cart,CartItem
from cart.views import _get_quote_id
from django.core.exceptions import ObjectDoesNotExist


def get_cart_item_total(request):
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(quote_id=_get_quote_id(request))
            if request.user.is_authenticated:
                cart_items = CartItem.objects.all().filter(user=request.user)
            else:
                cart_items = CartItem.objects.filter(cart=cart[:1])
            item_total = cart_items.count()
        except Cart.DoesNotExist:
            item_total = 0
    return dict(item_total=item_total)