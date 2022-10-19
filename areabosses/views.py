from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import AreaBossesForm
from .models import AreaBosses
# Create your views here.

class CreateAreaBoss(generic.CreateView):
    template_name = "areabosses/create_areabosses.html"
    model = User
    form_class = UserCreationForm