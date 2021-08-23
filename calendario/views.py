from .models import Calendarioferiado
import csv, io, os
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
# get or create https://docs.djangoproject.com/en/dev/ref/models/querysets/
with open(Calendarioferiado) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Calendarioferiado.objects.get_or_create(
                calendarioid=row[0],
                ano=row[1],
                mes=row[2],
                dia=row[3]
                )