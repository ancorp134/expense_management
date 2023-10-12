from django.contrib import admin
from .models import Employee , Budget, AdvanceTripPlan

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
  list_display = ("user","contract_no","contract_start_date","contract_end_date")
  list_filter = ("user","contract_no","contract_start_date","contract_end_date") 
  search_fields = ("contract_no","user",)


class BudgetAdmin(admin.ModelAdmin):
  list_display = ("employee","budget_amount","remaining_budget","budget_added","budget_modified")
  list_filter = ("employee__user__username",) 
  search_fields = ("employee__user__username",)


class AdvanceTripPlanAdmin(admin.ModelAdmin):
  list_display = ("employee","date_added","trip_plan")
  list_filter = ("employee__user__username","date_added") 
  search_fields = ("employee__user__username",)
  


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Budget,BudgetAdmin)
admin.site.register(AdvanceTripPlan,AdvanceTripPlanAdmin)
