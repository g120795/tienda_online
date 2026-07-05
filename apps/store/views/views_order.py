from django.shortcuts import render, redirect
from ..models.models_product import Product
from ..models.models_order_item import OrderItem
from ..models.models_order import Order
from apps.users.models import Profile
from ..form import OrderForm
from django.contrib.auth.decorators import login_required
from ..form import OrderItemForm


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    context = {
        'form':form
    }
    return render(request, 'create_order.html', context)


def create_order_item(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderItemForm()
    context = {
        'form':form
    }
    return render(request, 'create_order_item.html', context)

@login_required
def add_to_cart(request, product_id):
    
    a=f'cantidad: {request.POST.get('quantity',1)}'
    print(a)
    # product
    producto = Product.objects.get(id=product_id)
    order = Order.objects.filter(profile_id__user_id=request.user.id).first()
    #order and orderitem save
    # si la orden existe el if devuelve false y pasa al else
    if not order:
        formorder = OrderForm({'status': 'CART', 'order_total': float(request.POST.get('quantity', 1))*producto.product_price, 'profile': Profile.objects.get(user_id=request.user.id)})
        if formorder.is_valid():
            print('formorder is valid')
            formorder.save()
            formorderitem = OrderItemForm({'name_product': producto.product_name,
                                   'quantity': float(request.POST.get('quantity', 1)),
                                    'price_unit': producto.product_price,'subtotal': float(request.POST.get('quantity', 1))*producto.product_price, 'order': formorder.instance.id, 'product': producto.id})    
            if formorderitem.is_valid():
                print('formorderitem is valid')
                formorderitem.save()        
                return render(request, 'add_to_cart.html', {'text': 'Producto agregado al carrito'} )
    else:
        order = Order.objects.filter(profile_id__user_id=request.user.id).first()
        order_item = OrderItem.objects.get(product_id=product_id)          
        print(f'id: {order_item.id}')
        print(order_item.quantity)
        cantidad=request.POST.get('quantity')
        print(f'cantidad: {cantidad}')
        if order_item:
            print('entrando al primer if')
            cantidad=request.POST.get('quantity')
            if order_item.quantity == cantidad:
                print('segundo if')
                return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  
            elif order_item.quantity != cantidad:
                print('elif')
                formitem = OrderItemForm({  'name_product': order_item.name_product,
                                            'quantity': float(request.POST.get('quantity')),
                                            'price_unit': order_item.price_unit,
                                            'subtotal': int(request.POST.get('quantity'))*float(order_item.price_unit), 
                                            'order': order.id, 
                                            'product': producto.id}, instance=order_item)
                print(formitem.errors)
                if formitem.is_valid():
                    formitem.save()
                    print('guardando')
                    return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  
                return redirect('detail_product', product_id)
        else:    
            if not order_item.exists():
                print('tercer if')
                formorderitem = OrderItemForm({'name_product': producto.product_name,
                                           'quantity': float(request.POST.get('quantity', 1)),
                                            'price_unit': producto.product_price,'subtotal': float(request.POST.get('quantity', 1))*producto.product_price, 'order': order.id, 'product': producto.id})    
                if formorderitem.is_valid():
                    print('formorderitem is valid')
                    formorderitem.save()        
                    return render(request, 'add_to_cart.html', {'text': 'Producto agregado al carrito'} )
        return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  
            
#status=status_choices
#created_at=fecha
#order_total=unit_price*quantity
#profile=users_profile
#
#product
#product_name
#product_model 
#product_price 
#product_current_stock 
#product_min_stock 
#category 
#
#orderitem
#
#name_product=product_name 
#quantity =cantidad que elige el usuario
#price_unit=product_price
#subtotal=quantity * price_unit
#order 
#product 