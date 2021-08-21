from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Calendario, Calendarioferiado

admin.site.register(Calendarioferiado)
admin.site.register(Calendario)