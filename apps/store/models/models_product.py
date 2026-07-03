from django.db import models
from .models_category import Category

# Product model
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_price = models.PositiveIntegerField()
    product_current_stock = models.PositiveIntegerField()
    product_min_stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    