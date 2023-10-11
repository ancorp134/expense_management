from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid
# Create your models here.


class Employee(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE,editable=False)
    contract_no = models.CharField(unique=True,max_length=15,null=True)
    contract_start_date = models.DateField(null=True)
    contract_end_date = models.DateField(null=True)
    phone_number = models.CharField(unique=True,max_length=10,null=True)
    profile_pic = models.ImageField(default="images/default.avif", upload_to="profile_pic")
    state = models.CharField(null=True,max_length=30)

    def __str__(self):
        return str(self.user)
    


class Budget(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    budget_added = models.DateField(auto_now_add=True)
    budget_modified = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.employee)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
        

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()
    
