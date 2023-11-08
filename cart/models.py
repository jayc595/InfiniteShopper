from django.db import models
from store.models import Product


# Create your models here.

class Cart(models.Model):
    quote_id = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quote_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    qty = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.product_price * self.qty

    def __unicode__(self):
        return self.product
