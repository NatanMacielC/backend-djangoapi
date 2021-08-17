from rest_framework import viewsets, serializers
from .models import Calendario, FeriadoCalendario
from fullcalendar import serializers

# Create your views here.
class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = serializers.CalendarSerializer

class FeriadoViewSet(viewsets.ModelViewSet):
    queryset = FeriadoCalendario.objects.all()
    serializer_class = serializers.FeriadoSerializer

