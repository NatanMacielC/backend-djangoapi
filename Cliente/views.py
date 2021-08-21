from rest_framework import viewsets, serializers
from .models import Grupo, Cliente, ClienteCliente
from cliente import serializers

# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

class ClienteclienteViewSet(viewsets.ModelViewSet):
    queryset = ClienteCliente.objects.all()
    serializer_class = serializers.ClienteClienteSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = serializers.GrupoSerializer

