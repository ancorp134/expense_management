from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()

@login_required(login_url='login')
def dashboard(request):
    try:
        user = User.objects.get()
    except:
        pass
    return render(request,'dashboard.html')

@login_required(login_url='login')
def profileView(request):
    user = request.user
    context ={
        'user' : user
    }
    return render(request,'profile.html' , context)