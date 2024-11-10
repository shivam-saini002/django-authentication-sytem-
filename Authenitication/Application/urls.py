from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.signn),
    path('loginn/', views.loginn),
    path('signup/', views.signup),
    path('home/', views.home),
    
]
