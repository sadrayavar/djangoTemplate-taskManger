from django.db import models
from user.models import User
from task.models import Task
from datetime import datetime, time


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    @property
    def datetime(self):
        return datetime.combine(self.date, self.time)

    # replyTo = models.OneToOneField(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)