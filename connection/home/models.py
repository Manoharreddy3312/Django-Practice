from django.db import models

# Create your models here.

class Employee_details(models.Model):
    name = models.CharField(max_length=32)
    phone = models.BigIntegerField(default=9876543210)
    doj = models.DateField(default='2000-01-01')
    description = models.TextField(default='Java Developer')
    email = models.EmailField(default='abc@gmail.com')
    sal = models.IntegerField(default=10000)
    
   
    
    
   

  

