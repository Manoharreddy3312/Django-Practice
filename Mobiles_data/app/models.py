from django.db import models


# Create your models here.

def stdnt_db(models.Models):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    battery = models


