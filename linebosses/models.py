from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class LineBosses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    line = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.user.first_name
