from importlib.metadata import files
from pyexpat import model
from attr import fields
from django import forms


from .models import SolicitudPiezas, RegistroDeEntrega


class PiezasForm(forms.ModelForm):
    class Meta:
        model = SolicitudPiezas
        fields = "__all__"

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroDeEntrega
        fields = ["lineboss","piece","no_order"]