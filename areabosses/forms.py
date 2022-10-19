from pyexpat import model
from django import forms
from django import forms

from .models import AreaBosses

class AreaBossesForm(forms.ModelForm):
    class Meta:
        model = AreaBosses
        fields = "__all__"