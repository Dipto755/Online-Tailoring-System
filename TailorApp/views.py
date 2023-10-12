from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import fabric_model
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    
    return render(request, 'home.html')

def login_view(request):
    
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['pass']
        
        theUser = authenticate(username = uname, password = pword)
        
        if theUser is not None:
            login(request, theUser)
            fname = theUser
            
            # next_url = request.GET.get('', '/')
            # return render(request, 'homepage.html', {'fname':fname})
            return redirect('homepage')
        else:
            messages.error(request, "Incorrect username or password!")
            return redirect('login')
        
    
    return render(request, 'login.html')

@login_required
def homepage_view(request):
    
    return render(request, 'homepage.html')

def signup_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        myuser.save()
        
        messages.success(request, "Your account has been successfully created.")
        
        return redirect('login')
    
    return render(request, 'signup.html')

def logout_views(request):
    logout(request)
    
    return redirect('home')

def fabric_view(request):
    fabric_list = fabric_model.objects.all()
    
    return render(request, 'fabric.html' ,
                {'fabric_list' : fabric_list})
    

@login_required
def update_profile_view(request):
    
    return render(request, 'update_profile.html')