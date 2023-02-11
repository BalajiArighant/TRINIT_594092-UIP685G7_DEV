from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import signup
from .models import user

# Create your views here.

def login_user(request):
	if request.method == 'POST':
		print("Post Data: ", request.POST)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
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
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']
		firstName = request.POST['first_name']
		lastName = request.POST['last_name']
		dateOfBirth = request.POST['dateOfBirth']
		userLocation = request.POST['userLocation']
		userDesc = request.POST['userDesc']
		model1 = user()
		if User.objects.filter(username = username).first():
			messages.error(request, "This username is already taken")
			return redirect('register')
		if password1 == password2:
			newUser = User.objects.create_user(
				username=username,
				email=email,
				password=password1,
				first_name=firstName,
				last_name=lastName
			)
			model1 = user()
			model1.userl = newUser
			model1.dob = dateOfBirth
			model1.userLocation = userLocation
			model1.userDesc = userDesc
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