from rest_framework import serializers
from  calendario import models

class CalendarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Calendario
        fields = '__all__'

class CalendarioferiadoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.Calendarioferiado
        fields = '__all__'

class CalendarioferiadoimportSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = models.CalendarioFeriadoImport
        fields = '__all__'