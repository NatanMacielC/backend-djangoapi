from django.contrib import admin
from django.db import models

# Register your models here.

from .models import Regras, Evento

admin.site.register(Regras)
admin.site.register(Evento)