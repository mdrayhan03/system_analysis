from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    # path('', views.baseapp, name="baseapp"),
    path('', views.landpage, name="landpage"),
    path('login/', views.login, name="login"),
    path('createAccount/', views.createAccount, name="createAccount"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('map/', views.map, name="map"),
    path('mytrip/', views.mytrip, name="mytrip"),
    path('trip/', views.trip, name="trip"),
    path('history/', views.history, name="history"),
    path('feedback/', views.feedback, name="feedback"),
    path('emergency/', views.emergency, name="emergency"),
    path('profile/', views.profile, name="profile"),
    path('changeProfile/', views.changeProfile, name="changeProfile"),
]
