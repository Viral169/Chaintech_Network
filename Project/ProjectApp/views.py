from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from ProjectApp.models import Profile, Contact_us
from datetime import datetime
import random


# Create your views here.

def login_page(request):
    if request.method == "POST":
        # email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Email')
            return redirect('/login')

        usr = authenticate(username=username, password=password)
        if usr is None:
            messages.error(request, 'Invaild Email or Password')
            return redirect('/login')
        else:
            login(request, usr)
            return redirect('/')
    return render(request, 'login.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        username = request.POST.get('username')
        last_name = request.POST.get('lname')
        mobile_number = request.POST.get('mobile-number')
        email = request.POST.get('email')
        password = request.POST.get('password')

        emaill = User.objects.filter(email=email)
        if emaill.exists():
            messages.info(request, 'Email is already exists')
            return redirect('/signup')
        usr = User.objects.create(username=username, first_name=first_name,
                                  last_name=last_name, email=email, password=password)
        usr.set_password(password)
        usr.save()

        profile = Profile(user=usr, first_name=first_name,
                          last_name=last_name, email=email, mobile_number=mobile_number)
        profile.save()

        messages.info(request, 'Account Created Succefully')
        return redirect('/login')
    return render(request, "signup.html")


@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return redirect('/login')


def rendom_quots():
    quots = [
        'Be yourself everyone else is already taken.',
        '''I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.''',
        '''“So many books, so little time.”''',
        '''“So many books, so little time.”''',
        '''“A room without books is like a body without a soul.”''',
        '''“Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.”''',
        '''“You've gotta dance like there's nobody watching,Love like you'll never be hurt,Sing like there's nobody listening,And live like it's heaven on earth.”''',
    ]

    return random.choice(quots)


@login_required(login_url="/login")
def home(request):
    current_time = datetime.now()
    quots = rendom_quots()
    context = {
        "current_time": current_time,
        'quots': quots,
    }
    return render(request, "home.html", context)


@login_required(login_url="/login")
def contact_us(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        mesage = request.POST.get('message')
        contact = Contact_us(name=name, email=email,mobile_number=mobile, message=mesage)
        contact.save()
        messages.info(request,"We will mail or call you soon")
        return redirect('/')
    return render(request, 'contact-us.html')
