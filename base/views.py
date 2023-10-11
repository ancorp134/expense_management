from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from account.models import Employee,Budget,AdvanceTripPlan
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages

# Create your views here.
User = get_user_model()
@login_required(login_url='login')
def dashboard(request):
    try:
        employee = Employee.objects.get(user=request.user)
        budget = Budget.objects.get(employee=employee)
        
    except Budget.DoesNotExist:
        # Handle the case where no budget is found
        budget = 0 
    users = request.user

    context = {
        'user' : users,
        'employee' : employee,
        'budget' : budget
    }
    
    return render(request,'dashboard.html',context)

@login_required(login_url='login')
def profileView(request):
    employee = Employee.objects.get(user=request.user)
    print(employee)
    user = request.user
    context ={
        'user' : user,
        'employee' : employee
    }
    return render(request,'profile.html' , context)

@login_required(login_url='login')
def changePassword(request):
    if (request.method == "POST"):
        currPass = request.POST['current_password']
        newPass1 = request.POST['new_password1']
        newPass2 = request.POST['new_password2']

        user = authenticate(username = request.user.username, password = currPass)

        if user is not None:
            if newPass1 == newPass2 :
                request.user.set_password(newPass1)
                request.user.save()
                update_session_auth_hash(request,request.user)
                login(request,request.user)
                messages.success(request,"Password changed successfully")
                return redirect('profile')
            else:
                messages.error(request,"Passwords do not match")
                return redirect('profile')

        else:
            messages.error(request,"current password is incorrect")
            return redirect('profile')

        
    return render(request,'profile.html')


@login_required(login_url='login')
def advancetravelPlan(request):
    if request.method == 'POST':
        trip_plan_file = request.FILES.get('trip_plan')
        employee = Employee.objects.get(user=request.user)
        trip=AdvanceTripPlan.objects.create(
                employee=employee,
                trip_plan=trip_plan_file
        )
        print(trip)
        messages.success(request,"Trip Plan Added Successfully!")
        return redirect('dashboard')
    
    return redirect('dashboard')



def error404(request, exception):
    return render(request, '404.html')