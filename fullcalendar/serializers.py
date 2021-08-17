from rest_framework import serializers
from  fullcalendar import models

class CalendarSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Calendario
        fields = '__all__'

class FeriadoSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.FeriadoCalendario
        fields = '__all__'