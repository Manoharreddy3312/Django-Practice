from django.db import models

# Create your models here.

class Travels(models.Model):
    name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    
