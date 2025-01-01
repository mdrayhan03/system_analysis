from django.shortcuts import render, redirect
from . import database

# Create your views here.

def baseapp(request) :
    return render(request, "baseapp/baseapp.html")

def landpage(request) :
    return render(request, "baseapp/landpage.html")

def login(request) :
    if request.method == "POST" :
        email = request.POST.get("email")
        password = request.POST.get("password")
        rider = database.rider
        driver = database.driver
        user = None
        if (rider["email"] == email and rider["password"] == password) :
            user = rider 
        elif (driver["email"] == email and driver["password"] == password) :
            user = driver

        request.session["user"] = user
        return redirect("baseapp:dashboard")

    return render(request, "baseapp/login.html")

def createAccount(request) :
    return render(request, "baseapp/createAccount.html")

def dashboard(request) :
    user = request.session["user"]
    return render(request, "baseapp/dashboard.html", {"user" : user})

def map(request) :
    return render(request, "baseapp/map.html")


def mytrip(request) :
    user = request.session["user"]
    return render(request, "baseapp/mytrip.html", {"user" : user})

def history(request) :
    user = request.session["user"]
    return render(request, "baseapp/history.html", {"user" : user})

def feedback(request) :
    return render(request, "baseapp/feedback.html")

def emergency(request) :
    return render(request, "baseapp/emergency.html")

def profile(request) :
    user = request.session["user"]
    return render(request, "baseapp/profile.html", {"user" : user})

def changeProfile(request) :
    user = request.session["user"]
    return render(request, "baseapp/changeProfile.html", {"user" : user})