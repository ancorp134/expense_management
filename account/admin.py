from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("user","contract_no","contract_start_date","contract_end_date")


admin.site.register(Employee,EmployeeAdmin)
