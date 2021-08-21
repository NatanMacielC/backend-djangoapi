from rest_framework import serializers
from  empresa import models

class EmpresasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresa
        fields = '__all__'

class EmpresaplanocontasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresaplanocontas
        fields = '__all__'

class PlanocontasEmpresaplanocontasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanocontasEmpresaplanocontas
        fields = '__all__'

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedor
        fields = '__all__'

class GrupoempresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grupoempresa
        fields = '__all__'