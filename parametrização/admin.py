from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Regra, Evento

admin.site.register(Regra)
admin.site.register(Evento)