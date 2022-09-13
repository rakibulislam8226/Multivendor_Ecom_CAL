from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    address=models.TextField(null=True)
    def __str__(self) -> str:
        return self.user.username
    
class ProductCategory(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField(null=True)
    def __str__(self) -> str:
        return self.title
    
    
class Product(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField(null=True)
    price=models.FloatField(max_length=5)
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True)
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.title)
    
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.user.username
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.customer.user.username)


class OrderItems(models.Model):
    product=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.product.user.username
    
