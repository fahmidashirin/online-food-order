from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length = 20)
    image = models.ImageField(upload_to="profilepic")

    def __str__(self):
        return str(self.user)
    
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity

    
class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        total_price = self.product.price * self.quantity
        return total_price


    






