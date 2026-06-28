from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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


