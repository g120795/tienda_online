from django.shortcuts import render
from ..form import ProductForm
from django.contrib.auth.decorators import login_required

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'create_product.html', context)