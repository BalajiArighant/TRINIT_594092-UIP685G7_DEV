from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signup
from .models import user
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your views here.

def login_user(request):
	if request.method == 'POST':
		print("Post Data: ", request.POST)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		print("Username", username)
		print("Password: ", password)
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		
		else:
			messages.success(request, message="Incorrect username/password")
			return redirect('login')
	else:
		return render(request, "login.html")



def register_user(request):
	form = signup(request.POST)
	if request.method == 'POST':
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		model1 = user()
		if password1 == password2:
			model1.save()
			messages.success(request, message="User created successfully!")
			return redirect('login')
		
		else:
			messages.success(request, message="Passwords do not match. Please try again")
			return render(request, 'register.html', {'form': form})


	else:
		return render(request, 'register.html', {'form': form})



def logout_user(request):
	logout(request)
	messages.success(request, message="Logged out successfully!")
	return redirect('login')