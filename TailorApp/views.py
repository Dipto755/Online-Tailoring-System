from django.shortcuts import render, HttpResponse

# Create your views here.

def home_view(request):
    
    return render(request, 'home.html')

def login_view(request):
    
    return render(request, 'login.html')

def signup_view(request):
    
    return render(request, 'signup.html')
