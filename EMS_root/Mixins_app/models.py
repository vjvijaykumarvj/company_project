from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age =models.IntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name