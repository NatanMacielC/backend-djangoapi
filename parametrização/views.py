from rest_framework import viewsets, serializers
from .models import Regra, Evento
from parametrização import serializers

# Create your views here.
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = serializers.EventoSerializer

class RegrasViewSet(viewsets.ModelViewSet):
    queryset = Regra.objects.all()
    serializer_class = serializers.RegraSerializer