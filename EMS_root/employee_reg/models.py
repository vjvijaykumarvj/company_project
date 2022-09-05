from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class common(models.Model):
    firstname = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    address = models.TextField(max_length=1000)

    class Meta:
        abstract = True

class Contact(common):
    write_some = models.TextField(max_length=2000)

    def __str__(self):
        return self.firstname,'+',self.lastname

class Employee_model(common):
    password = models.CharField(max_length=30,unique=True)
    c_password = models.CharField(max_length=30,unique=True)
    username = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.username

