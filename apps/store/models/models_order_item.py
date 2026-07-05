from django.db import models
from .models_order import Order
from .models_product import Product
from django.core.validators import MinValueValidator

class OrderItem(models.Model):
    name_product = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price_unit = models.DecimalField(max_digits=10,decimal_places=2)
    subtotal = models.DecimalField(max_digits=10,decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True) # CONSERVAR ORDERITEM
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True) # CONSERVA ORDERITEM

    def __str__(self):
        return f'{self.name_product}'
    