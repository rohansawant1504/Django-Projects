from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Emp_no','Emp_name','Emp_sal','Emp_city']


admin.site.register(Employee,EmployeeAdmin)
