from asyncio.format_helpers import _format_callback_source
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import SolicitudPiezas, RegistroDeEntrega
from Procesos import views as P
from django.contrib.auth.decorators import login_required
from .forms import PiezasForm, RegistroForm, UpdateRegistroForm
# Create your views here.


class SPiezas(generic.CreateView):
    template_name = "Procesos/SolicitarPiezas.html"
    model = SolicitudPiezas
    form_class = PiezasForm
    success_url = reverse_lazy("solicitud_piezas")


class EntregaAlmacen(generic.CreateView):
    template_name = "Procesos/EntregaDeAlmacen.html"
    model = RegistroDeEntrega
    form_class = RegistroForm
    success_url = reverse_lazy("registros_piezas")


class UpdateEntregaAlmacen(generic.UpdateView):
    template_name = "Procesos/UpdateEntregaDeAlmacen.html"
    model = RegistroDeEntrega
    form_class = UpdateRegistroForm
    success_url = reverse_lazy("registros_piezas")