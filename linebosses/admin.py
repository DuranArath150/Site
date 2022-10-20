from django.contrib import admin
from .models import LineBosses

# Register your models here.


@admin.register(LineBosses)
class LineBossesAdmin(admin.ModelAdmin):
    list_display = ["user","line"]