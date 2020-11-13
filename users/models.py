from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_member = models.BooleanField('member status', default=False)
    is_coach = models.BooleanField('member status', default=False)
    is_admin = models.BooleanField('member status', default=False)


class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Admin: " + str(self.user)


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Coach: " + str(self.user)


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.RESTRICT)

    def __str__(self):
        return "Member: " + str(self.user)
