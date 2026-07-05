from django import forms
from ..models import OrderItem


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = [
                    'name_product',
                    'quantity',
                    'price_unit',
                    'subtotal',
                    'order',
                    'product',
                    
                    
        ]
