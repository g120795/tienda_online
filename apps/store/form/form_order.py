from django import forms
from ..models import Order
from ..models import OrderItem

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
                    'order_num', 
                    'order_date', 
                    'order_total', 
                    'profile'
                  ]

