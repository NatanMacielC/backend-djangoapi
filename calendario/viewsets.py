from rest_framework import viewsets, serializers
from .models import Calendario, Calendarioferiado
from calendario import serializers

# Create your views here.

class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = serializers.CalendarioSerializer

class CalendarioferiadoViewSet(viewsets.ModelViewSet):
    queryset = Calendarioferiado.objects.all()
    serializer_class = serializers.CalendarioferiadoSerializer


