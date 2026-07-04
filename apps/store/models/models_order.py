from django.db import models
from apps.users.models import Profile

class Order(models.Model):
    STATUS_CHOICES = (
        ('CART', 'Carrito'),
        ('PAID', 'Pagado'),
        ('SHIPPED', 'Enviado'),
        ('DELIVERED', 'Entregado'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CART')
    created_at = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) # SE CONSERVA ORDER

    def __str__(self):
        return f'{self.profile.user.username} - {self.status} - {self.created_at}'
    

"""
falta agregar
*estado del pedido
"""
