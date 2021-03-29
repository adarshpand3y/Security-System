from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserDetails, Report
import datetime
from django.contrib import messages

# messages.success(request, 'This is my message')

# My Views

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
            userdetails = UserDetails(username=username, adhaar_number=adhaar, phone_number=phone)
            userdetails.save()
            messages.success(request, "User created successfully. Now log in with the details provided.")
        else:
            messages.error(request, "There was some error in form data, please try again.")
    return redirect('/')

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

def dashboard(request):
    if request.user.is_authenticated:
        reports = Report.objects.filter(submitted_by=request.user).order_by("-timeStamp")
        context = {"reports": reports, "len": len(reports)}
        return render(request, 'dashboard.html', context)
    else:
        messages.info(request, "You must log in to submit a report.")
        return redirect("/")

def check_username(request):
    username = request.GET.get("un")
    print(username)
    print(User.objects.filter(username = username).exists())
    if User.objects.filter(username = username).exists():
        print("PRESENT")
    else:
        print("NOT PRESENT")
    return redirect('/')

def submit_report(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, "submitreport.html")
    else:
        title = request.POST.get("report_title")
        body = request.POST.get("report_body")
        user = request.POST.get("user")
        print(title, user, body)
        report = Report(title=title, content=body, submitted_by=user, timeStamp=datetime.datetime.now(), status="Submitted")
        report.save()
        messages.success(request, 'Your report was submitted sucessfully.')
    return(redirect("/"))