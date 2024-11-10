from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import sign
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.messages import constants as messages

# Create your views here.



def signn(request):
    return render(request,'sign.html')

def signup(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        sign(name=name,email=email,password=password).save()
        ms="sign up sucessfully"
        return render(request,"login.html",{'ms':ms})
    
    else:
  
        HttpResponse("<h1>Eroor 400</h1>")
     
     

def loginn(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email,password=password)
        print(user)
        
        if(user is not None):
            auth_login(request,user)
            return HttpResponseRedirect("home/")
        else:
            print("galat mt dal")
            return HttpResponseRedirect("/loginn")
            
    else:
        return HttpResponse("error")
          
    

        
        
def home(request):
    return HttpResponse("<h1>Home page succesfull login</h1>")        