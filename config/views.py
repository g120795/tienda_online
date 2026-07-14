from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,'home.html')
@login_required
def features(request):
    return render(request, 'features.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')
@login_required
def product(request):
    return render(request, 'product.html')
@login_required
def staff_link(request):
    return render(request, 'staff_link.html')
@login_required
def order(request):
    return render(request, 'order.html')
@login_required
def catalog_link(request):
    return render(request, 'catalog_link.html')
@login_required
def seller_function(request):
    return render(request, 'seller_function.html')

