from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterationForm(UserCreationForm):
    # email=forms.EmailField(max_length=50)
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
