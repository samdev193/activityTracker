import django.contrib.auth
from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.forms import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userprofile", null=True)
    exercise = models.IntegerField()
    work = models.IntegerField()
    relax = models.IntegerField()
    study = models.IntegerField()
    self_care = models.IntegerField()

    def __str__(self):
        return self.user
