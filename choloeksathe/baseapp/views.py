from django.shortcuts import render

# Create your views here.

def baseapp(request) :
    return render(request, "baseapp/baseapp.html")