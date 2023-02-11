from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import user, NGO, Projects

class signup(UserCreationForm):
	dateOfBirth = forms.DateField(label='Date of Birth')
	userLocation = forms.CharField(label='Your city:')
	userDesc = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20, 'label': 'Introduce yourself (Mention any donation preferences that you may have)'}))

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'dateOfBirth', 'email', 'userLocation', 'userDesc']
	