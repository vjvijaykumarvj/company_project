from django.db import models

# Create your models here.
type = [('AC','AC'),('Non AC','Non AC'),('King','King'),('Primier','Premier')]
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    room_no = models.IntegerField()
    room_type= models.CharField(max_length=10,choices=type,default='AC')
    images = models.ImageField(upload_to='media',width_field=None,height_field=None)

    def __str__(self):
        return self.name
