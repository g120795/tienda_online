from django.shortcuts import render
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


def cart(request,user_id, product_id):


    return render(request, 'cart.html')

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