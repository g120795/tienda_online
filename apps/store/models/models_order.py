from django.db import models
from apps.users.models import Profile

class Order(models.Model):
    STATUS_CHOICES = (
        ('CART', 'Carrito'),
        ('PAID', 'Pagado'),
        ('SHIPPED', 'Enviado'),
        ('DELIVERED', 'Entregado'),
    )
    PAYMENT_CHOICES = (
        ('deposito','Deposito'),
        ('transferencia','Transferencia'),
        ('yape','Yape'),
        ('efectivo','Efectivo'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CART')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True) # SE CONSERVA ORDER

    def __str__(self):
        return f'{self.status} - {self.created_at} - {self.payment_method} - {self.profile} - {self.order_total}'
    