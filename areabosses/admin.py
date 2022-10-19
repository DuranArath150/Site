from django.contrib import admin
from .models import AreaBosses
# Register your models here.


@admin.register(AreaBosses)
class AreaBossesAdmin(admin.ModelAdmin):
    list_display = ["user","area"]