from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
from taskManager.settings import EMAIL_HOST_USER
from .models import Task
from emailpaper.models import Newspaper


taskCount = Task.objects.count()


def getTaskCount():
    global taskCount
    return taskCount


@receiver(post_save, sender=Task)
def taskAddHandler(sender, instance, created, *args, **kwargs):
    print(f"New Task has been added: {instance.title}")
    global taskCount
    if created:
        taskCount += 1
        print("########################", f"Task {instance.title} is created.\n")
        email_generator(instance)


@receiver(post_delete, sender=Task)
def taskDeleteHandler(sender, instance, *args, **kwargs):
    print(f"{instance.title} task deleted.")
    global taskCount
    taskCount -= 1
    print("########################", f"Task {instance.title} is removed.\n")


def email_generator(instance):
    from_email = EMAIL_HOST_USER
    recipient_list = [email.email for email in Newspaper.objects.filter(active=True)]
    subject = "Hello from HERISI Task Manager"
    message = [
        "New task has been added to HERISI Task Manager.\n",
        "Check it out in the link below and feel free to write a comment.\n",
        "\n",
        f"http://127.0.0.1:8000/{instance.id}\n",
    ]

    send_mail(subject, "".join(message), from_email, recipient_list)
