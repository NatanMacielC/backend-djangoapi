from rest_framework import viewsets
from empresas.api import serializers
from empresas import models

class EmpresasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresasSerializer
    queryset = models.Empresas.objects.all()