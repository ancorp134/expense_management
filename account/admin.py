from django.contrib import admin
from .models import Employee , Budget

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("user","contract_no","contract_start_date","contract_end_date")


class BudgetAdmin(admin.ModelAdmin):
  list_display = ("employee","budget_amount","remaining_budget","budget_added","budget_modified")


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Budget,BudgetAdmin)
