from django.shortcuts import render, redirect
from . import database
import requests

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

def trip(request) :
    fr = "Independent University Bangladesh"
    to = "Mirpur-2"
    frcoordinates = list(get_coordinates(fr))
    tocoordinates = list(get_coordinates(to))

    coordinates = {
        "from" : frcoordinates,
        "to" : tocoordinates
    }    
    return render(request, "baseapp/triptrack.html", {"coordinates" : coordinates})

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

def get_coordinates(place_name):
    api_key = 'f20ec4be93844a14b1b9f9c7db770cb3'
    url = f'https://api.opencagedata.com/geocode/v1/json?q={place_name}&key={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            coords = data['results'][0]['geometry']
            return coords['lat'], coords['lng']
        else:
            return "No results found"
    else:
        return f"Error: {response.status_code}"