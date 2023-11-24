from django.db import models


# Create your models here.
class Task(models.Model):
    STATE_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=50)
    priority = models.IntegerField()
    state = models.CharField(max_length=11, choices=STATE_CHOICES)
    deadline = models.DateTimeField()
