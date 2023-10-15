from django.contrib import admin
from store.models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_sku', 'product_slug', 'product_category', 'product_price',
                    'product_special_price', 'product_stock', 'is_available', 'created_at', 'updated_at')
    prepopulated_fields = {'product_slug': ('product_name',)}


admin.site.register(Product, ProductAdmin)
