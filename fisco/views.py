from rest_framework import viewsets, serializers
from .models import Fisco
from fisco import serializers

# Create your views here.
class FiscoViewSet(viewsets.ModelViewSet):
    queryset = Fisco.objects.all()
    serializer_class = serializers.FiscoSerializer