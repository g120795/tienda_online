from django.shortcuts import render
from ..form import CategoryForm

def create_category(request):
    if request.method == 'POST':
        print('entrando al primer if')
        form = CategoryForm(request.POST)
        if form.is_valid():
            print('entrando al segundo if')
            form.save()
    else:
        form = CategoryForm
    context = {

        'form':form
    }
    return render(request, 'create_category.html', context)