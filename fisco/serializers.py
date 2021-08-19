from rest_framework import serializers
from fisco import models

class FiscoSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Fisco
        fields = '__all__'

