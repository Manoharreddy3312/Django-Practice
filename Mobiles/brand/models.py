from django.db import models

# Create your models here.


# class Brand_db(models.Model):
#     name = models.CharField(max_length=100)
#     brand = models.CharField(max_length=100)
#     price = models.IntegerField()
#     battery = models.CharField(default="5000mAh", max_length=100)
#     # ram = models.CharField(max_length=100)
#     # rom = models.CharField(max_length=100)
#     # display = models.CharField(default="6.1 AMOLED", max_length=100)
#     # camera = models.CharField(default="12MP", max_length=100)
#     # processor = models.CharField(default="Snapdragon", max_length=100)
#     # warranty = models.CharField(default="1 Year", max_length=100)
   

#     def __str__(self):
#         return self.name

class Mobiles(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    battery = models.IntegerField()

    def __str__(self):
        return self.name

   

