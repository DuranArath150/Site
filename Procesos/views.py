from asyncio.format_helpers import _format_callback_source
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views import generic
from .models import SolicitudPiezas, RegistroDeEntrega
from Procesos import views as P
from .forms import PiezasForm, RegistroForm
# Create your views here.


class SPiezas(generic.CreateView):
    template_name = "Procesos/SolicitarPiezas.html"
    model = SolicitudPiezas
    form_class = PiezasForm


class EntregaAlmacen(generic.CreateView):
    template_name = "Procesos/EntregaDeAlmacen.html"
    model = RegistroDeEntrega
    form_class = RegistroForm