from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    username = forms.CharField(label=(""),widget=forms.TextInput(attrs={'class' : 'btn-login', 'placeholder':'Username'}))
    email = forms.EmailField(label=(""),widget=forms.TextInput(attrs={'class' : 'btn-login','placeholder':'Email'}))
    password1 = forms.CharField(label=(""),
                        widget=forms.PasswordInput(attrs={'class' : 'btn-login', 'placeholder':'Password'}))
    password2 = forms.CharField(label=(""),
                            widget=forms.PasswordInput(attrs={'class' : 'btn-login', 'placeholder':'Password Confirmation'}))
    class Meta:
        model = User
        fields = ("username",'email','password1','password2')
