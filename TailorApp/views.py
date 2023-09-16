from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home_view(request):
    
    return render(request, 'home.html')

def login_view(request):
    
    return render(request, 'login.html')

def signup_view(request):
    
    return render(request, 'signup.html')
