from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.urls import reverse
# Create your views here.



def loginview(request):
    
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            context ={'user': user}
            return redirect(reverse('dashboard'),context)
        
        return messages.error(request,"Invalid credentials")

    return render(request,"login.html")

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect(reverse('login'))
