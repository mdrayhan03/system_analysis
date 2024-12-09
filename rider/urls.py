from django.urls import path
from . import views

app_name = "rider"

urlpatterns = [
    # path('', views.baseapp, name="baseapp"),
    path('', views.dashboard, name="dashboard"),
    path('map/', views.map, name="map"),
    path('ride/', views.ride, name="ride"),
]
