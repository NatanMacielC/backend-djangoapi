from rest_framework import serializers
from planocontas import  models

class PlanocontasPlanocontasreferencialSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.PlanocontasPlanocontasreferencial
        fields = '__all__'

class PlanocontasreferencialSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.Planocontasreferencial
        fields = '__all__'