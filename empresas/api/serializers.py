from rest_framework import serializers
from  empresas import models

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresas
        fields = '__all__'