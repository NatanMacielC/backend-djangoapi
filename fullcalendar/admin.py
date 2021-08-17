from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Calendario, FeriadoCalendario

admin.site.register(FeriadoCalendario)
admin.site.register(Calendario)