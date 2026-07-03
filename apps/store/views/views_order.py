from django.shortcuts import render
from ..form import OrderForm
from django.contrib.auth.decorators import login_required

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

