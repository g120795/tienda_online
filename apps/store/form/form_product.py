from django import forms
from ..models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
                 'product_name', 
                 'product_model', 
                 'product_price', 
                 'product_current_stock', 
                 'product_min_stock',
                 'category'
                 
                 ]