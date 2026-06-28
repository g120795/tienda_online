from django.shortcuts import render
from ..form import CategoryForm
from django.contrib.auth.decorators import login_required

@login_required
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