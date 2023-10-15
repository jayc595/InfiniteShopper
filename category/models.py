from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    # category_slug = models.CharField(max_length=100, unique=True)
    category_description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='images/category', blank=True)

    # we use the below to define the plural name, without this Django admin will make it 'categorys' by default.
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_slug_url(self):
        return reverse('products_by_category', args=[self.category_slug])

    def __str__(self):
        return self.category_name
