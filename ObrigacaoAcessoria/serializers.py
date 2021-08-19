from rest_framework import serializers
from  ObrigacaoAcessoria import models

class ObrigacaoAcessoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObrigacaoAcessoria
        fields = '__all__'