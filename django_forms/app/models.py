from django.db import models

# Create your models here.

class Gender(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class Qualification(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Religion(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    



class Scholorship(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    aadhar_number = models.CharField(max_length=12)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    pan_number = models.CharField(max_length=10)
    email = models.EmailField()
    income = models.CharField(max_length=20)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    address = models.TextField()
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    degree_percentage = models.DecimalField(max_digits=4, decimal_places=1)













    


