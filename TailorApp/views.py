from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import fabric_model, user_model, contact_model, type_model, design_kameez_model, design_salowaar_model, design_shirt_model, measureForSalwar_model, measurementForKameez_model,measurementForShirt_model, kameez_order_model, salowaar_order_model, shirt_order_model
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
            # return redirect('homepage', fname = fname)
            return redirect('homepage')
            # return render(request, 'homepage.html', {fname})
            # url = "homepage/?user={}".format(fname)
            # return redirect(url)
        else:
            messages.error(request, "Incorrect username or password!")
            return redirect('login')
        
    
    return render(request, 'login.html')

@login_required
def homepage_view(request):
    # fname = request.GET.get('fname', None)
    # return render(request, 'homepage.html', {'fname' : fname})
    # if request.method == "GET":
    #     fname = request.GET.get('user')
    # return render(request, 'homepage.html', {'fname' : fname})
    if request.user.is_authenticated:
        username = request.user.username
        
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        contact = contact_model(cont_name = name, cont_email = email, cont_message = message)
        contact.save()
        
        return redirect('homepage')
    return render(request, 'homepage.html', {'username':username})

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

# def contact_views(request):
    

@login_required
def fabric_view(request):
    fabric_list = fabric_model.objects.all()
    
    return render(request, 'fabric.html' , {'fabric_list' : fabric_list})

@login_required
def user_details_view(requset):

    # if requset.user.is_authenticated:
        
    #     return render(requset, 'user_details.html')
    # else:
    #     return redirect('login')
    data = user_model.objects.get(user__id = requset.user.id)
    
    return render(requset, 'user_details.html', {'data' : data})


@login_required
def type_view(request, pk):
    
    if request.user.is_authenticated:
        username = request.user.username
    
    fab = fabric_model.objects.filter(pk = pk).first()
    type_list = type_model.objects.all()
    
    global val_fab
    def val_fab():
        return fab
    
    context = {'fab' : fab, 'type_list' : type_list, 'username':username}
    
    return render (request, 'type.html', context)

@login_required
def design_view(request,pk):
    # fab = fabric_model.objects.filter(pk = pk).first()
    type = type_model.objects.filter(pk = pk).first().ty_id
    kameez_design_list = design_kameez_model.objects.all()
    salowaar_design_list = design_salowaar_model.objects.all()
    shirt_design_list = design_shirt_model.objects.all()
    
    
    # type_id = val_type()
    context = {'type' : type, 'kameez_design_list' : kameez_design_list, 'salowaar_design_list':salowaar_design_list, 'shirt_design_list':shirt_design_list, 'type_id' : type}

    # fab = val_fab()
    
    # global val_fab
    # def val_fab():
    #     return fab
    
    global val_type
    def val_type():
        return type
    
    return render(request, 'design.html', context)

def design_view_all(request):
    # fab = fabric_model.objects.filter(pk = pk).first()
    # type = type_model.objects.filter(pk = pk).first().ty_id
    kameez_design_list = design_kameez_model.objects.all()
    salowaar_design_list = design_salowaar_model.objects.all()
    shirt_design_list = design_shirt_model.objects.all()
    
    
    # type_id = val_type()
    context = {'kameez_design_list' : kameez_design_list, 'salowaar_design_list':salowaar_design_list, 'shirt_design_list':shirt_design_list}

    # fab = val_fab()
    
    # global val_fab
    # def val_fab():
    #     return fab
    
    
    return render(request, 'design_all.html', context)


@login_required
def update_profile_view(request):
    context = {}
    data = user_model.objects.get(user__id = request.user.id)
    context["data"] = data
    
    if request.user.is_authenticated:
        username = request.user.username
    
    if request.method == "POST":
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        em = request.POST["email"]
        add = request.POST["address"]
        nmbr = request.POST["number"]
        gndr = request.POST["gender"]
        
        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        
        usr.save()
        
        data.u_address = add
        data.u_cont_number = nmbr
        data.u_gender = gndr
        
        data.save()
    return render(request, 'update_profile.html', {'username':username})

@login_required
def measurement_kameez_views(request):
    # context = {}
    # data = measurementForKameez_model()
    # context["data"] = data
    if request.method == "POST":
        ln = request.POST["length"]
        bln = request.POST["body"]
        sln = request.POST["shoulder"]
        wln = request.POST["waist"]
        hln = request.POST["hip"]
        handwth = request.POST["hand_length"]
        nln = request.POST["neck_length"]
        nwth = request.POST["neck_width"]
        
        data = measurementForKameez_model(k_length = ln, k_body_length = bln, k_shoulder_length=sln, k_waist_length=wln, k_hip_length=hln,k_hand_width=handwth,k_neck_length=nln, k_neck_width = nwth)
        
        data.save()
        
    
    return render(request, 'measurement_kameez.html')

@login_required
def measurement_salowaar_view(request):
    
    if request.method == "POST":
        ln = request.POST["length"]
        wln = request.POST["waist"]
        hln = request.POST["hip"]
        tln = request.POST["thigh"]
        wth = request.POST["width"]
        
        data = measureForSalwar_model(sl_length = ln, sl_waist_length=wln, sl_hip_length=hln,sl_thigh_length=  tln, sl_width=wth)
        
        data.save()
    
    return render(request, 'measurement_salowaar.html')

@login_required
def measurement_shirt_view(request):
    
    if request.method == "POST":
        cln = request.POST["c_length"]
        slln = request.POST["s_length"]
        sln = request.POST["shoulder"]
        bcp = request.POST["bicep"]
        chst=request.POST["chest_length"]
        hln = request.POST["hip_length"]
        
        
        data = measurementForShirt_model(s_collar_length = cln, s_sleeve_length = slln, s_shoulder_length=sln, s_bicep=bcp,s_chest_length=chst,s_hip_length=hln)
        
        data.save()
    
    return render(request, 'measurement_shirt.html')

@login_required
def d_details_kameez_view(request, pk):
    design_id = design_kameez_model.objects.filter(pk = pk).first().dk_id
    design_list = design_kameez_model.objects.filter(dk_id = design_id).first()
    # design_list = design_kameez_model.objects
    # print(design_list.first().dk_id)
    global val_design_id
    def val_design_id():
        return design_id
    
    context = {'design_id' : design_id, 'design_list' : design_list}
    
    return render(request, 'd_destails_kameez.html', context)

@login_required
def d_details_salowaar_view(request, pk):
    design_id = design_salowaar_model.objects.filter(pk = pk).first().ds_id
    design_list = design_salowaar_model.objects.filter(ds_id = design_id).first()
    # design_list = design_kameez_model.objects
    # print(design_list.first().dk_id)
    global val_design_id
    def val_design_id():
        return design_id
    
    context = {'design_id' : design_id, 'design_list' : design_list}
    
    return render(request, 'd_destails_salwar.html', context)
    
    # return render(request, 'd_destails_salwar.html')

@login_required
def d_details_shirt_view(request):
    
    
    
    return render(request, 'd_destails_shirt.html')

@login_required
def order_confirm_payment_view(request):
    
    # f_id = val_fab()
    # d_id = val_design_id()
    # order_type = val_type()
    # # des_id = design_kameez_model.objects.filter(dk_id = d_id).first().dk_id
    # if order_type == 1:
        
    #     orderConf = kameez_order_model(f_id = f_id, o_type="Kameez")
    #     orderConf.dk_id = d_id
        
    #     orderConf.save()
    
    
    return render(request, 'payment_method.html')

def payment_method(request):
    
    return render (request, 'payment.html')