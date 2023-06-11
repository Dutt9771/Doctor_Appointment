from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images', max_length=None)
    speciality = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    doctor = models.CharField(max_length=50)


class Service(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images', max_length=None)

    def __str__(self):
        return self.name
