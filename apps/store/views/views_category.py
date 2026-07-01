from django.shortcuts import render, redirect
from ..form import CategoryForm
from django.contrib.auth.decorators import login_required

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog_link')
    else:
        form = CategoryForm
    context = {

        'form':form
    }
    return render(request, 'create_category.html', context)