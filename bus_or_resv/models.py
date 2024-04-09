from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Srcdst(models.Model):
    source=models.CharField(max_length=50)
    dest=models.CharField(max_length=50)
    

class Bus(models.Model):
    bus_name= models.CharField(max_length=50)
    bus_number= models.CharField(max_length=50)
    bus_image=models.ImageField(upload_to='bus_images')
    srcdst= models.ForeignKey(Srcdst, on_delete=models.CASCADE)
    source_time=models.TimeField(auto_now=False, auto_now_add=False)
    dest_time=models.TimeField(auto_now=False, auto_now_add=False)
    source_date=models.DateField()
    dest_date=models.DateField()
    seat= models.IntegerField()
    price=models.IntegerField()

class Reservation(models.Model):
    bus= models.ForeignKey(Bus, on_delete=models.CASCADE)
    # c_name= models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    c_id_proof=models.ImageField(upload_to='id_images')
    seat=models.IntegerField()
    total_price=models.IntegerField()
    status=models.CharField(max_length=50)
