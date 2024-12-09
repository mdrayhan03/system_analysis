from django.shortcuts import render

# Create your views here.

def baseapp(request) :
    return render(request, "baseapp/baseapp.html")

def landpage(request) :
    return render(request, "baseapp/landpage.html")

def login(request) :
    return render(request, "baseapp/login.html")

def createAccount(request) :
    return render(request, "baseapp/createAccount.html")