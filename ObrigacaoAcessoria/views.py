from rest_framework import viewsets
from ObrigacaoAcessoria import serializers, models

class ObrigacaoAcessoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObrigacaoAcessoriaSerializer
    queryset = models.ObrigacaoAcessoria.objects.all()