from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .form import UserForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_success.html')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)



def staff(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = UserForm(instance=user)
    context = {

        'form':form
    }
    return render(request, 'staff.html',context)
