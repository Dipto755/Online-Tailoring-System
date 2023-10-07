from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
            fname = theUser.first_name
            return render(request, 'homepage.html', {'fname':fname})
        else:
            messages.error(request, "Incorrect username or password!")
            return redirect('login')
        
    
    return render(request, 'login.html')

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