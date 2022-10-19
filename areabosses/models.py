from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class AreaBosses(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def ensure_areabosses_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        AreaBosses.objects.get_or_create(user=instance)