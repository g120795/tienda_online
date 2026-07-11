from django.shortcuts import render, redirect, get_object_or_404
from ..form import ProductForm, OrderItemForm
from django.contrib.auth.decorators import login_required
from ..models.models_product import Product

@login_required
def create_product(request):
    if not request.user.is_staff:
        return redirect('home')
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

def update_product(request, product_id):
    if not request.user.is_staff:
        return redirect('home')
    
    producto = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    else:
        form = ProductForm(instance=producto)
    context = {
        'form': form
    }
    return render(request, 'update_product.html',context)

@login_required
def seller_catalog(request):
    if not request.user.is_staff:
        return redirect('home')
    
    productos = Product.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'seller_catalog.html', context)

@login_required
def seller_detail_product(request, product_id):
    if not request.user.is_staff:
        return redirect('home')
    
    producto = Product.objects.get(id=product_id)
    context = {
        'producto': producto,
    }
    print(context)

    return render(request, 'seller_detail_product.html', context)

def delete_product(request,product_id):
    producto = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('seller_catalog')
    context = {
        'producto':producto
    }
    return render(request, 'delete_product.html',context)


@login_required
def catalog(request):
    productos = Product.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'catalog.html', context)

@login_required
def detail_product(request, product_id):
    print(request)
    stock_disponible = 0
    producto = Product.objects.get(id=product_id)
    stock_disponible = f'{producto.product_current_stock - producto.product_min_stock:.0f}'
    form = OrderItemForm({'quantity': 1})
    context = {
        'producto': producto,
        'stock_disponible': stock_disponible,
        'form': form,
    }
    print(context)

    return render(request, 'detail_product.html', context)

def update_stock(request,order_item):
    for i in order_item:
        print(i.product_id)
    for update in order_item:
        product = Product.objects.get(id=update.product_id)
        print(product)
        form = ProductForm({'product_name':product.product_name,
                            'product_model':product.product_model,
                            'product_price':product.product_price,
                            'product_current_stock':product.product_current_stock-update.quantity,
                            'product_min_stock':product.product_min_stock,
                            'category':product.category},instance=product)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('cart')
        else:
            return redirect('payment')