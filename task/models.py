from django.db import models
from datetime import datetime, date, time
from django.core.validators import MinValueValidator
from user.models import User


# Create your models here.
class Task(models.Model):
    STATE_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=15, unique=True)
    priority = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    state = models.CharField(max_length=11, choices=STATE_CHOICES, default="New")
    deadline_date = models.DateField(default=date.today)
    deadline_time = models.TimeField(default=time(0, 0, 0))

    @property
    def deadline(self):
        return datetime.combine(self.deadline_date, self.deadline_time)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
