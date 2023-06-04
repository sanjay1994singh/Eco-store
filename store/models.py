from django.db import models
from django.contrib.auth.models import User

class LookupField(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='brand_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

class Brand(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='brand_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    discount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Additional fields
    brand = models.ForeignKey('store.Brand', on_delete=models.PROTECT)
    category = models.ForeignKey('store.Category', on_delete=models.PROTECT)
    stock = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User,models.PROTECT)
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
