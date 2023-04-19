from django.db import models

# Create your models here.

class Product(models.Model):
    
    name = models.CharField(max_length=100)
    price = models.FloatField(default=10000)
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()
    
    
    
class Category (models.Model):
    
    name = models.CharField(max_length=100)
    
    