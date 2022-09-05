from django.db import models

# Create your models here.
class Library(models.Model):
    books = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    departmant = models.CharField(max_length=20)

    def __str__(self):
        return self.books

class Book(models.Model):
    book_name = models.ForeignKey(Library,on_delete=models.CASCADE)
    auther = models.CharField(max_length=20)
    study = models.CharField(max_length=20)

    def __str__(self):
        return self.auther
