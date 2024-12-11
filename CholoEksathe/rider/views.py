from django.shortcuts import render
import requests

# Create your views here.
def dashboard(request) :
    return render(request, "rider/dashboard.html")

def map(request) :
    return render(request, "rider/map.html")

def ride(request) :
    place = "Dhaka"
    coordinates = get_coordinates(place)
    print(f"Coordinates of {place}: {coordinates}")

    return render(request, "rider/ride.html")

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