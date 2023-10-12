from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
import uuid
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.conf import settings
# Create your models here.


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,editable=True)
    full_name = models.CharField(max_length= 50)
    email = models.EmailField(max_length=50)
    contract_no = models.CharField(unique=True,max_length=15,)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField()
    phone_number = models.CharField(unique=True,max_length=10)
    profile_pic = models.ImageField(default="images/default.avif", upload_to="profile_pic")
    state = models.CharField(max_length=30)

    def __str__(self):
        return str(self.user)
    


class Budget(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    budget_added = models.DateField(auto_now_add=True)
    budget_modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.employee)
    

def get_upload_path(instance,filename):
    return os.path.join('Advance Trip Plans/' +  str(instance.employee.user.username),filename)

    
class AdvanceTripPlan(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = models.CharField(choices = [
        ('January', 'January'),
        ('February', 'February'),
        ('March' , 'March'),
        ('April','April'),
        ('May','May'),
        ('June','June'),
        ('July','July'),
        ('August','August'),
        ('September','September'),
        ('October','October'),
        ('November','November'),
        ('December','December')
    ],default = "January",max_length=10)
    year = models.CharField(max_length=20,default = "2023",null=True)
    date_added = models.DateField(auto_now_add=True)
    trip_plan = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return str(self.employee)





@receiver(post_save, sender=Employee)
def send_reset_password_link(sender, instance, created, **kwargs):
    if created:
        # Generate a unique token for the user
        token = default_token_generator.make_token(instance.user)
        
        # Create a password reset link
        uid = urlsafe_base64_encode(force_bytes(instance.user.pk))
        reset_url = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        
        # Construct the password reset URL
        site_domain = 'http://localhost:8000'  # Replace with your domain
        reset_link = f'http://{site_domain}{reset_url}'
        
        # Send the password reset link to the user's email
        subject = 'Password Reset Request'
        message = f'Hello {instance.full_name},\n\n Your username is {instance.user.username} \n\nYou can reset your password by clicking on the following link:\n{reset_link}'
        from_email = settings.EMAIL_HOST_USER   # Replace with your email address
        recipient_list = [instance.email]
        
        send_mail(subject, message, from_email, recipient_list)


