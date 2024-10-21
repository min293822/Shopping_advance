from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
  name = models.CharField(max_length=200)
  price = models.IntegerField()
  image = models.FileField(upload_to='images')
  
  def __str__(self):
    return self.name

class Cart(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  completed = models.BooleanField(default=False)
  
  @property
  def total(self):
    cartitems = self.cartitems.all()
    total = sum([item.each_total for item in cartitems])
    return total
    
  @property
  def item_number(self):
    cartitems = self.cartitems.all()
    quantity = sum([item.quantity for item in cartitems])
    return quantity
  
  def __str__(self):
    return str(self.id)

class CartItems(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
  cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
  quantity = models.IntegerField(default=0)
  
  @property
  def each_total(self):
    total_price = self.product.price * self.quantity
    return total_price
    
  def __str__(self):
    return self.product.name
  
  
  