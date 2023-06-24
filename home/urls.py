from django.contrib import admin
from django.urls import path
from home import views as home_views

app_name = 'home' #add o app_name para deixaer mais seguro e dinamico 

urlpatterns = [
    path('', home_views.home, name = 'home' ), 
]
