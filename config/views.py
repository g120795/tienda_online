from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def features(request):
    return render(request, 'features.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def category(request):
    return render(request, 'category.html')

def order(request):
    return render(request, 'order.html')


