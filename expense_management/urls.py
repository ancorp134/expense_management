"""expense_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account.views import loginview,logoutview
from base.views import dashboard , profileView , changePassword ,advancetravelPlan,actualTripPlan
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
handler404 = 'base.views.error404'



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/login',loginview,name='login'),
    path('logout/',logoutview,name="logout"),
    path('',dashboard,name="dashboard"),
    path('dashboard/profile',profileView,name='profile'),
    path('dashboard/profile/changepassword/',changePassword,name="changePassword"),
    path('dashboard/advance_travel_plan/',advancetravelPlan,name="advancetravelplan"),
    path('dashboard/actual_trip_plan/',actualTripPlan,name="actualTripplan"),
    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

