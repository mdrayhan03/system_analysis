from django.shortcuts import render

# Create your views here.
def ride(request) :  
    return render(request, "driver/ride.html")