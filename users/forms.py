from django import forms
from django.forms import ModelForm
from .models import user, NGO, Projects

class signup(forms.Form):
	username = forms.CharField(max_length=45, label='Username')
	password1 = forms.CharField(max_length=150, widget=forms.PasswordInput, label='Password')
	password2 = forms.CharField(max_length=150, widget=forms.PasswordInput, label='Confirm Password')
	first_name = forms.CharField(max_length=30, label='First Name')
	last_name = forms.CharField(max_length=30, label='Last Name')
	dateOfBirth = forms.DateField(label='Date of Birth')
	email = forms.EmailField(label='Email Address')
	userLocation = forms.CharField(label='Your city:')
	userDesc = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20, 'label': 'Introduce yourself (Mention any donation preferences that you may have)'}))