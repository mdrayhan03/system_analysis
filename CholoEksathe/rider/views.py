from django.shortcuts import render
import requests

# Create your views here.
def ride(request) :
    fr = "Independent University Bangladesh"
    to = "Mirpur-2"
    frcoordinates = list(get_coordinates(fr))
    tocoordinates = list(get_coordinates(to))

    coordinates = {
        "from" : frcoordinates,
        "to" : tocoordinates
    }    
    return render(request, "rider/ride.html", {"coordinates" : coordinates})

def shareride(request) :
    fr = "Independent University Bangladesh"
    to = "Mirpur-2"
    frcoordinates = list(get_coordinates(fr))
    tocoordinates = list(get_coordinates(to))

    coordinates = {
        "from" : frcoordinates,
        "to" : tocoordinates
    }  

    return render(request, "rider/shareride.html", {"coordinates" : coordinates})

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

def reserve(request) :
    fr = "Independent University Bangladesh"
    to = "Mirpur-2"
    frcoordinates = list(get_coordinates(fr))
    tocoordinates = list(get_coordinates(to))

    coordinates = {
        "from" : frcoordinates,
        "to" : tocoordinates
    }
    return render(request, "rider/reserve.html", {"coordinates" : coordinates})

def community(request) :
    return render(request, "rider/community.html")

def message(request) :
    return render(request, "rider/message.html")