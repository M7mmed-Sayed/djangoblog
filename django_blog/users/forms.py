from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserRegisterationForm(UserCreationForm):
    # email=forms.EmailField(max_length=50)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class UpdateUserInfo(forms.ModelForm):
    # email=forms.EmailField(max_length=50)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name']


class UpdateUserProfile(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['image']
