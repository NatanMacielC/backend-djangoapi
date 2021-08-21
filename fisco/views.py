from rest_framework import viewsets, serializers
from .models import Fisco, Fiscocalendario
from fisco import serializers

# Create your views here.
class FiscoViewSet(viewsets.ModelViewSet):
    queryset = Fisco.objects.all()
    serializer_class = serializers.FiscoSerializer

class FiscocalendarioViewSet(viewsets.ModelViewSet):
    queryset = Fiscocalendario.objects.all()
    serializer_class = serializers.FiscocalendarioSerializer