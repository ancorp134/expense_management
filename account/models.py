from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
import uuid
# Create your models here.


class Employee(AbstractUser):
    username = None
    last_login = None
    groups = None
    user_permissions=None
    
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField(unique=True , max_length=40)
    contract_no = models.CharField(unique=True,max_length=15,null=True)
    contract_start_date = models.DateField(null=True)
    contract_end_date = models.DateField(null=True)
    phone_number = models.CharField(unique=True,max_length=10,null=True)
    profile_pic = models.ImageField(default="images/default.avif", upload_to="profile_pic")
    state = models.CharField(null=True,max_length=30)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email 
