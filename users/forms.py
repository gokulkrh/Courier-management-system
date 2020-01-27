from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	Amrita_mail = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'Amrita_mail', 'password1', 'password2']