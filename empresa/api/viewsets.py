from rest_framework import viewsets
from empresa.api import serializers
from empresa import models

class EmpresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresasSerializer
    queryset = models.Empresa.objects.all()

class EmpresaplanocontasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaplanocontasSerializer
    queryset = models.Empresaplanocontas.objects.all()

class FornecedorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FornecedorSerializer
    queryset = models.Fornecedor.objects.all()

class GrupoempresaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GrupoempresaSerializer
    queryset = models.Grupoempresa.objects.all()

class PlanocontasEmpresaplanocontasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PlanocontasEmpresaplanocontasSerializer
    queryset = models.PlanocontasEmpresaplanocontas.objects.all()