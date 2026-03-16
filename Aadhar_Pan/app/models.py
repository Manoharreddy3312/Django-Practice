from django.db import models

class Gender(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class State(models.Model):
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name


class User_Data(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    father=models.CharField(max_length=50)

    aadhar = models.CharField(max_length=12, unique=True, null=True, blank=True)
    pan = models.CharField(max_length=10, null=True, blank=True)

    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    state=models.ForeignKey(State,on_delete=models.CASCADE)

    dob=models.DateField()
    phone=models.PositiveIntegerField()
    address=models.TextField()
    city=models.CharField(max_length=20)

    image=models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.first_name