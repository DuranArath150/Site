from email.policy import default
from random import choices
from unicodedata import name
from django import forms
from django.db import models
from django.contrib.auth.models import User

from linebosses.models import LineBosses

from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
# Create your models here.

CHOICES = (
    ("P1", "PIEZA 1"),
    ("P2", "PIEZA 2"),
    ("P3", "PIEZA 3"),
)

class SolicitudPiezas(models.Model):
    piece = models.CharField(max_length=32, default="PIEZA 1", choices=CHOICES)
    cantdad_pieza = models.IntegerField(default=0, blank = False , null = False)

    def __str__(self):
        return self.user.first_name


class RegistroDeEntrega(models.Model):
    name = models.CharField(max_length = 32,blank=False, null=False)
    lineboss = models.OneToOneField(LineBosses, on_delete=models.CASCADE)
    piece = models.CharField(max_length= 32 , default = "PIEZA 1", choices = CHOICES)
    no_order = models.IntegerField(default = "0", blank = False , null = False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name


