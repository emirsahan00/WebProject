from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label='User name :')
    first_name = forms.CharField(max_length=50,help_text='First name',label='First name :')
    last_name = forms.CharField(max_length=50,help_text='Last name',label='Last name :')
    email = forms.EmailField(max_length=100,label='Email :')

    class Meta:
        model = User
        fields = {'username','first_name','last_name','email','password1','password2'}