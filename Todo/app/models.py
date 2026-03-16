from django.db import models

# Create your models here.
class Todo_data(models.Model):
    Task = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)



class History_Table(models.Model):
    Task = models.CharField(max_length=20)
    Description = models.CharField(max_length=100)