from django.db import models


# User = get_user_model()
class Newspaper(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
