from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    photo = models.ImageField(upload_to = "studentpics")
