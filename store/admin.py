from django.contrib import admin
from store.models import Product, ProductOptions, ProductOptionTitle


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_sku', 'product_slug', 'product_category', 'product_price',
                    'product_special_price', 'product_stock', 'is_available', 'created_at', 'updated_at')
    prepopulated_fields = {'product_slug': ('product_name',)}


class ProductOptionTitleAdmin(admin.ModelAdmin):
    list_display = ('option_title', 'option_title_frontend', 'option_code', 'option_type', 'created_at', 'updated_at',
                    'is_active')
    prepopulated_fields = {
                            'option_code': ('option_title',),
                            'option_title_frontend': ('option_title',)
                           }


class ProductOptionsAdmin(admin.ModelAdmin):
    list_display = ('product_option_titles', 'product_option_value', 'product', 'created_at', 'updated_at', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductOptionTitle, ProductOptionTitleAdmin)
admin.site.register(ProductOptions,ProductOptionsAdmin)
