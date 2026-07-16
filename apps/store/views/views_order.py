from django.shortcuts import render, redirect
from ..models.models_product import Product
from ..models.models_order_item import OrderItem
from ..models.models_order import Order
from apps.users.models import Profile
from ..form import OrderForm
from django.contrib.auth.decorators import login_required
from ..form import OrderItemForm
from .views_product import update_stock

@login_required
def create_order(request):
    if not request.user.is_staff:
        return redirect('home')
    
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
    if not request.user.is_staff:
        return redirect('home')
    
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
    perfil = Profile.objects.get(user_id=request.user.id)

    # product
    producto = Product.objects.get(id=product_id)
    order = Order.objects.filter(profile_id__user_id=request.user.id, status='CART').first()

    cantidad = int(request.POST.get('quantity'))
    if cantidad < 1 or cantidad > (producto.product_current_stock-producto.product_min_stock):
        return redirect('detail_product',product_id)
    #order and orderitem save
    # si la orden existe el if devuelve false y pasa al else
    if not order:
        formorder = OrderForm({'status': 'CART',
                               'profile': perfil.id})
        if formorder.is_valid():
            formorder.save()
            formorderitem = OrderItemForm({'name_product': producto.product_name,
                                    'quantity': float(request.POST.get('quantity')),
                                    'price_unit': producto.product_price,
                                    'subtotal': float(request.POST.get('quantity', 1))*producto.product_price,
                                    'order': formorder.instance.id, 
                                    'product': producto.id})    
            if formorderitem.is_valid():
                formorderitem.save()        
                return render(request, 'add_to_cart.html', {'text': 'Producto agregado al carrito'} )
        else:
            return redirect('detail_product',product_id)    
    else:
        order_item = OrderItem.objects.filter(product_id=product_id).first()
        if order_item:
            cantidad=request.POST.get('quantity')
            if order_item.quantity == cantidad:
                return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  
            elif order_item.quantity != cantidad:
                formitem = OrderItemForm({  'name_product': order_item.name_product,
                                            'quantity': float(request.POST.get('quantity')),
                                            'price_unit': order_item.price_unit,
                                            'subtotal': int(request.POST.get('quantity'))*float(order_item.price_unit), 
                                            'order': order.id, 
                                            'product': producto.id}, instance=order_item)
                if formitem.is_valid():
                    formitem.save()
                    return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  
                return redirect('detail_product', product_id)
        else:
                formorderitem = OrderItemForm({ 'name_product': producto.product_name,
                                                'quantity': float(request.POST.get('quantity', 1)),
                                                'price_unit': producto.product_price,
                                                'subtotal': float(request.POST.get('quantity', 1))*producto.product_price, 
                                                'order': order.id, 
                                                'product': producto.id})    
                
                if formorderitem.is_valid():
                    formorderitem.save()        
                    return render(request, 'add_to_cart.html', {'text': 'Producto agregado al carrito'} )
        return render(request, 'add_to_cart.html', {'text': 'El producto ya se encuentra en el carrito'} )  

@login_required
def cart(request):
    order = Order.objects.filter(profile_id__user_id=request.user.id,status='CART').first()
    if not order:
        return render(request, 'cart.html',{'order':'carrito vacio'})    
    orderitem = OrderItem.objects.filter(order_id=order.id, product__is_active=True)
    total = 0 
    for i in orderitem:
        if i.subtotal:
            total+=i.subtotal
    context = {
        'orderitem':orderitem,
        'total': total
    }
    return render(request, 'cart.html', context)

@login_required
def pay_method(request):
    order = Order.objects.filter(profile_id__user_id=request.user.id,status='CART').first()
    if request.method == 'POST':
        form = OrderForm({
                            'profile':order.profile_id,
                            'status':order.status,
                            'payment_method':request.POST.get('payment_method')},
                            instance=order)
        if form.is_valid():
            form.save()
            return redirect('payment')

    else:
        form = OrderForm()
    context={
        'form':form,
    }
    return render(request, 'pay_method.html', context)

@login_required
def payment(request):
    order = Order.objects.filter(profile_id__user_id=request.user.id, status='CART').first()
    order_item =OrderItem.objects.filter(order_id=order.id, product__is_active=True)
    total = 0
    for subtotal in order_item:
        if subtotal.subtotal:
            total += subtotal.subtotal
    if request.method=='POST':
        order_form = OrderForm({'order_total':total,
                                'profile':order.profile_id,
                                'status':'PAID',
                                'payment_method':order.payment_method},
                                instance=order)
        if order_form.is_valid():
            order_form.save()
            update_stock(order_item)
            return redirect('catalog')
        else:
            return redirect('pay_method')
    context = {
        'order':order,
        'order_item':order_item,
        'total':total,
     }
    return render(request, 'payment.html',context)

@login_required
def list_order(request):
    if not request.user.is_staff:
        return redirect('home')
    order = Order.objects.all()
    context = {

        'order':order
    }
    return render(request, 'list_order.html', context)



def mi_orders(request):
    #lista_item = []
    #order_id = []
    #order_item = OrderItem.objects.filter(order__profile__user_id=request.user.id)
    #for i in order_item:
    #    order_id.append(i.order_id)
    #order_id=list(set(order_id))
#
    #for i in range(0,len(order_id)):
    #    lista = []
    #    for j in order_item:  
    #        if order_id[i] == j.order_id:  
    #            lista.append(j)
    #    lista_item.append(lista)
    orders = Order.objects.filter(profile__user_id=request.user.id).prefetch_related('orderitem_set')
    context = {
        'orders':orders,
    }
    return render(request, 'mi_orders.html', context)












