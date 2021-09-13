from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    telephone = models.CharField(max_length=16)
