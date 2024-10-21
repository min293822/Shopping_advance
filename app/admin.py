from django.contrib import admin
from .models import Product, Cart, CartItems

admin.site.register(Product)
admin.site.register(CartItems)
admin.site.register(Cart)