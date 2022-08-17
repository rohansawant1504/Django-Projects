from django.db import models

# Create your models here.
class students(models.Model):
    Roll_No = models.IntegerField(primary_key=True)
    Student_Name = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Email = models.EmailField()
    Date_of_admission = models.DateTimeField()
    # Record = models.DateField(auto_now_add=True)
