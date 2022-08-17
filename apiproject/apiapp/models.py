from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_no = models.IntegerField(primary_key=True)
    Emp_name = models.CharField(max_length=30)
    Emp_sal = models.IntegerField()
    Emp_city = models.CharField(max_length=30)