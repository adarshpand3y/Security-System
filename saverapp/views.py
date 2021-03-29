from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserDetails

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    return render(request, 'login.html')

def handleSignup(request):
    if request.method=="POST":
        # Get the post parameters
        firstname = request.POST.get('register_firstname')
        lastname = request.POST.get('register_lastname')
        username = request.POST.get('register_username')
        email = request.POST.get('register_email')
        phone = str(request.POST.get('register_phone'))
        adhaar = str(request.POST.get('register_adhaar'))
        password = request.POST.get('register_password')
        conf_password = request.POST.get('register_conf_password')

        # check for errorneous input
        
        # Create the user
        if password == conf_password:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstname
            myuser.last_name = lastname
            myuser.save()
            # userdetails = 
        return redirect('home')

    else:
        return HttpResponse("There was an error in the form data. Please correct the data and try again.")

def handleLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST.get('login_username')
        loginpassword = request.POST.get('login_password')

        user = authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return redirect("/")

    return HttpResponse("404- Not found")

def handleLogout(request):
    if request.method == "POST":
        logout(request)
    return redirect('/')

def handleRegister(request):
    if request.method == "POST":
        # Get the post parameters
        firstname = request.POST.get("register_firstname")
        lastname = request.POST.get("register_lastname")
        username = request.POST.get("register_username")
        email = request.POST.get("register_email")
        phone = request.POST.get("register_phone")
        adhaar = request.POST.get("register_adhaar")
        password = request.POST.get("register_password")
        conf_password = request.POST.get("register_conf_password")

        print(firstname)
        print(lastname)
        print(username)
        print(email)
        print(phone)
        print(adhaar)
        print(password)
        print(conf_password)

        # Create the user
        if password == conf_password:
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name= firstname
            myuser.last_name= lastname
            myuser.save()
            details = UserDetails(username=username, adhaar_number=adhaar, phone_number=phone)
            details.save()
        return redirect('/dashboard')

    else:
        return HttpResponse("404 - Not found")

def dashboard(request):
    return render(request, 'dashboard.html')