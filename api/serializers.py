from rest_framework import serializers
from app.models import Product, Cart, CartItems

class ProductSerializer(serializers):
  class Meta:
    model = Product
    fields = '__all__'

class CartSerializer(serializers):
  class Meta:
    model = Cart
    fields = '__all__'

class CartItemsSerializer(serializers):
  class Meta:
    model = CartItems
    fields = '__all__'