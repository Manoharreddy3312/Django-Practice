from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class AccountType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Account(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    dob = models.DateField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=12, unique=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='customers/')
    pin = models.IntegerField(null=True, blank=True)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name