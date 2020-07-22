from django.forms import ModelForm
from .models import order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class orderForm(ModelForm):
	class Meta:
		model = order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class meta:
		model = User
		fields = ['username','email','password1','password2']