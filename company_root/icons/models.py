from django.db import models

# Create your models here.
class Student(models.Model):
    firstname = models . CharField(max_length=100)
    lastname = models . CharField(max_length=100)
    gender = models . CharField(max_length=100)
    age = models . IntegerField()
    contactnumber = models . IntegerField()
    emailid = models . CharField(max_length=100)
    address = models . CharField(max_length=100)
    city = models . CharField(max_length=100)
    state = models . CharField(max_length=100)
    python = models . CharField(max_length=100)
    bigdata = models . CharField(max_length=100)
    datascience = models . CharField(max_length=100)
    username = models . CharField(max_length=100)
    password = models . CharField(max_length=100)

