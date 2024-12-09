from django.urls import path
from . import views

app_name = "baseapp"

urlpatterns = [
    # path('', views.baseapp, name="baseapp"),
    path('', views.landpage, name="landpage"),
    path('login/', views.login, name="login"),
    path('createAccount/', views.createAccount, name="createAccount"),
]
