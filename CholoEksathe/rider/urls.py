from django.urls import path
from . import views

app_name = "rider"

urlpatterns = [
    # path('', views.baseapp, name="baseapp"),

    path('ride/', views.ride, name="ride"),
    path('shareride/', views.shareride, name="shareride"),
    path('reserve/', views.reserve, name="reserve"),

    path('community/', views.community, name="community"),
    path('message/', views.message, name="message"),

]
