from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField('max_digits=10')
    copies = models.IntegerField()
    

    

