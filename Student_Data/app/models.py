from django.db import models

class Student_Db(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    dob = models.DateField()
    
    qualification = models.CharField(max_length=100, null=True, blank=True)
    stream = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

# Create your models here.
