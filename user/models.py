from django.db import models

# Create your models here.


class userInfo(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)

class userTasks(models.Model):
    title = models.CharField(max_length=50)
    deadLine = models.DateTimeField()
