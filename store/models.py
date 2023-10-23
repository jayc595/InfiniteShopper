from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    product_slug = models.SlugField(max_length=200, unique=True)
    product_sku = models.CharField(max_length=25, unique=True)
    product_description = models.CharField(max_length=500, blank=True)
    product_price = models.IntegerField()
    product_special_price = models.IntegerField(default=0)
    product_images = models.ImageField(upload_to='images/products', blank=True)
    product_stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    # @TODO: the below on_delete will delete the product if the category exists, we should consider changing this
    #        for example we could add to a review style category and set the product to not be available.
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_product_url(self):
        return reverse('product_detail', args=[self.product_category.category_slug, self.product_slug])

    def __str__(self):
        return self.product_name


type_options = (
    ('dropdown', 'dropdown'),
)


class ProductOptionTitle(models.Model):
    option_title = models.CharField(max_length=100)
    option_code = models.SlugField(max_length=200, unique=True)
    option_title_frontend = models.CharField(max_length=100)
    option_type = models.CharField(max_length=100, choices=type_options)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product option title"
        verbose_name_plural = "product option title"

    def __str__(self):
        return self.option_title


class ProductOptions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_option_titles = models.ForeignKey(ProductOptionTitle, on_delete=models.CASCADE)
    product_option_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product option"
        verbose_name_plural = "product options"

    def __unicode__(self):
        return self.product




