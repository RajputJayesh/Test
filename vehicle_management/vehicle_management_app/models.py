from django.db import models

# Create your models here.
class record(models.Model):

    CH=((1,'Two Wheeler'),(2,'Three Wheeler'),(3,'Four Wheeler'))
    num=models.CharField(max_length=10,verbose_name="Vehicle Number")
    vehicletype=models.IntegerField(choices=CH,verbose_name="Vehicle Type")
    vehiclemodel=models.CharField(max_length=50,verbose_name="Vehicle Model")
    vehicledes=models.CharField(max_length=500,verbose_name="Vehicle Description")