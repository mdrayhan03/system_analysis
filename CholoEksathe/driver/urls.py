from django.urls import path
from . import views

app_name = "driver"

urlpatterns = [
    path('ride/', views.ride, name="ride"),
]
