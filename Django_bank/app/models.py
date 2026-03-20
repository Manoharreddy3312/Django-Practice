from django.db import models


class Acc_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class RelationShip(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Acc_creation(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    adress = models.TextField(max_length=50)
    dob = models.DateField()
    acc_number = models.IntegerField(default=12345678901)
    nominee = models.CharField(max_length=20)
    pin = models.IntegerField(default=0)
    balance = models.PositiveIntegerField(default=1000)
    acc_type = models.ForeignKey(Acc_type, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    relationship = models.ForeignKey(RelationShip, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"