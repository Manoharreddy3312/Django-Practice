from django.db import models

# Create your models here.

class Movies_db(models.Model):
    name = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    budget = models.PositiveIntegerField()

    
    def __str__(self):
      return self.name