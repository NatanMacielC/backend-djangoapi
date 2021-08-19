from rest_framework import serializers
from parametrização import models

class EventoSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Evento
        fields = '__all__'

class RegraSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.Regra
        fields = '__all__'