from django.db import models
from django.contrib.auth.models import User
# from employee_reg.models import Employee_model


class Employee(models.Model):
    # username = models.ForeignKey(Employee_model,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    eno = models.IntegerField()
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    address  =models.CharField(max_length=500)

    def __str__(self):
        return 'Employee,'+ str(self.firstname)
