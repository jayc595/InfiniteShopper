from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_item_from_cart/<int:product_id>/', views.remove_item_from_cart, name='remove_item_from_cart'),
    path('delete_item_from_cart/<int:product_id>/', views.delete_item_from_cart, name='delete_item_from_cart'),
]