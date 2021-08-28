from django.contrib import admin
from django.contrib.admin.decorators import display
from django.db import models

# Register your models here.

from .models import Calendario, Calendarioferiado, CalendarioFeriadoImport

admin.site.register(Calendarioferiado)

admin.site.register(Calendario)

admin.site.register(CalendarioFeriadoImport)
class CalendarioferiadoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'ano',
        'mes',
        'dia',
        'descricao',
    )
    search_fields = ('CalendarioferiadoAdmin')
    list_filter = ('descricao')