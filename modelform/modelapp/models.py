from django.db import models

# Create your models here.
class ModelFeedback(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()
    date = models.DateField()