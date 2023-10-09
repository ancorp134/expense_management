from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def register(request):
    if request.method == "POST":
        pass


def loginview(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        
        return messages.error(request,"Invalid credentials")

    return render(request,"login.html")

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect(reverse('login'))
