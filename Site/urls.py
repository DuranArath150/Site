
"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from Examen import views as Examen
from Procesos import views as Procesos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Examen.index, name="index"),   
    path('Solicitud_pieza/', Procesos.SPiezas.as_view(), name="solicitud_piezas"),
    path('Registro_piezas/', Procesos.EntregaAlmacen.as_view(), name = "registros_piezas"),
    path('UpdateRegistro_piezas/<int:pk>/', Procesos.UpdateEntregaAlmacen.as_view(), name='update_piezas'),

]
