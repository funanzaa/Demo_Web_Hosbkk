from django.urls import path
from .views import *



urlpatterns = [
    path('', HomePage , name = 'home-page'),
    path('Login', Login, name = 'login-page'),
    path('doLogin', doLogin, name = 'dologin-page'),
    path('staff_home', staff_home, name= 'staff_home') 
    
]