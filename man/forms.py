from django.contrib.auth.models import User
from django.forms import ModelForm
from.models import Room
from django.contrib.auth.forms import UserCreationForm
from django import forms
class Form(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']

class signupform(UserCreationForm):
    email=forms.CharField(max_length=100, required=True)   
    class Meta:
        model=User
        fields=['username','email','password1','password2']    
