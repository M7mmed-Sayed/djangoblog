from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            print(userName)
            form.save()
            messages.success(request, f'successful registration for {userName}! ')
            return redirect('blog-home')
    else:
        form = UserRegisterationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
