from django.db import models
from datetime import datetime, date, time
from django.core.validators import MinValueValidator


# Create your models here.
class Task(models.Model):
    STATE_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=50, unique=True)
    priority = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    state = models.CharField(max_length=11, choices=STATE_CHOICES)
    deadline_date = models.DateField(default=date.today)
    deadline_time = models.TimeField(default=time.min)

    @property
    def deadline(self):
        return datetime.combine(self.deadline_date, self.deadline_time)
