from django.db import models
from django.contrib.auth.models import User


# User = get_user_model()
class CustomUser(User):
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    newspaper = models.BooleanField(default=False)
