from django.urls import path
from . import views

app_name = "rider"

urlpatterns = [
    # path('', views.baseapp, name="baseapp"),
    path('', views.dashboard, name="dashboard"),
    path('map/', views.map, name="map"),
    path('ride/', views.ride, name="ride"),
    path('community/', views.community, name="community"),
    path('message/', views.message, name="message"),
    path('profile/', views.profile, name="profile"),
    path('changeProfile/', views.changeProfile, name="changeProfile"),
]
