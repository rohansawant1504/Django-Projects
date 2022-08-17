from django.contrib import admin
from .models import students


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['Roll_No','Student_Name','Address','Email','Date_of_admission']

admin.site.register(students,StudentAdmin)
