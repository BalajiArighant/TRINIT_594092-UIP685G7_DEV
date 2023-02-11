from django.shortcuts import render, redirect

# Write your views here

def home(request):
	return render(request, 'home.html')