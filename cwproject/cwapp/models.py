from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=25)
    pagenumber = models.IntegerField()
    publishDate = models.DateField
