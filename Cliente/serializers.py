from rest_framework import serializers
from  cliente import models

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Cliente
        fields = '__all__'

class ClienteClienteSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.ClienteCliente
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Grupo
        fields = '__all__'