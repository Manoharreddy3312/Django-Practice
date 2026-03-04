from django.db import models

# Create your models here.

# Patients Data

class PatientsData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)


# Students Data

class sdata(models.Model):
    name = models.CharField(max_length=32)
    phone = models.BigIntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    sub = models.CharField(max_length=100)






    