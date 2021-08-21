from rest_framework import serializers
from fisco import models

class FiscoSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Fisco
        fields = '__all__'

class FiscocalendarioSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = models.Fiscocalendario
        fields = '__all__'

