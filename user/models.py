from django.db import models

# Create your models here.

Class userInfo(models.model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
