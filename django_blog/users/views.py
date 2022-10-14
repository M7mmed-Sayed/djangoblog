from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterationForm, UpdateUserProfile, UpdateUserInfo
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'successful registration for {userName}! you can login now ')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        info_form = UpdateUserInfo(request.POST, instance=request.user)
        profile_form = UpdateUserProfile(request.POST, request.FILES, instance=request.user.profile)
        if info_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            info_form.save()
            messages.success(request, f'successful updated ')
            return redirect('profile')


    else:
        info_form = UpdateUserInfo(instance=request.user)
        profile_form = UpdateUserProfile(instance=request.user)

    context = {'info_form': info_form, 'profile_form': profile_form}
    return render(request, 'users/profile.html', context)
