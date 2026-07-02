from django.shortcuts import render, redirect
from ..form import ProductForm
from django.contrib.auth.decorators import login_required
from ..models.models_product import Product

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'create_product.html', context)


@login_required
def catalog(request):
    productos = Product.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'catalog.html', context)

@login_required
def detail_product(request, product_id):
    producto = Product.objects.get(id=product_id)
    context = {
        'producto': producto
    }
    return render(request, 'detail_product.html', context)