from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Task

taskCount = Task.objects.count()


def getTaskCount():
    global taskCount
    return taskCount


@receiver(post_save, sender=Task)
def taskAddHandler(sender, instance, created, *args, **kwargs):
    print("object added")
    global taskCount
    if created:
        taskCount += 1
        print("########################", f"Task {instance.title} is created.\n")


@receiver(post_delete, sender=Task)
def taskDeleteHandler(sender, instance, *args, **kwargs):
    print("object deleted")
    global taskCount
    taskCount -= 1
    print("########################", f"Task {instance.title} is removed.\n")
