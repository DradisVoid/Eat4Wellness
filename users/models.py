from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    is_member = models.BooleanField('member status', default=False)
    is_coach = models.BooleanField('coach status', default=False)
    is_admin = models.BooleanField('admin status', default=False)


class Coach(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "Coach: " + str(self.user)


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.RESTRICT)

    def __str__(self):
        return "Member: " + str(self.user)

    def get_absolute_url(self):
        return reverse('member-detail-view', args=[str(self.id)])
