from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"Donate/index.html",{})

def register(request):
    return render(request,"Donate/register.html",{})

def login(request):
    return render(request,"Donate/login.html",{})

def Information(request):
    return render(request,"Donate/Information.html",{})



