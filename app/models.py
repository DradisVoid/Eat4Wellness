from django.conf import settings
from django.db import models


# Create your models here.

# user profile models
class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.RESTRICT)
