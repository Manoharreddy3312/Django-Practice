from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class To_do(models.Model):
    task = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.task