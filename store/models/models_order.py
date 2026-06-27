from django.db import models
from .models_user import User

class Order(models.Model):
    order_num = models.PositiveIntegerField()
    order_date = models.DateField(null=True, blank=True)
    order_total = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # SE CONSERVA ORDER

    def __str__(self):
        return f'{self.n_order}'
    