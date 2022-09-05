from django.db import models


class model_emp(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)
    def __str__(self):
        return self.username