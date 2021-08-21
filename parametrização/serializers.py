from rest_framework import serializers
from parametrização import  models 

class EventoSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Evento
        fields = '__all__'

class RegraSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = models.Regra
        fields = '__all__'

class CnaeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Cnae
        fields = '__all__'

class GeracaocreditoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Geracaocredito
        fields = '__all__'

class RetencaofonteSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Retencaofonte
        fields = '__all__'

class PeriodicidadeSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Periodicidade
        fields = '__all__'

class GrupoeventoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Grupoevento
        fields = '__all__'

class EventogrupoSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = models.Eventogrupo
        fields = '__all__'

class ParametrizacaoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.Parametrizacao
        fields = '__all__'

class ParametrizacaoregraSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Parametrizacaoregra
        fields = '__all__'

class CodigoprefeituraSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.Codigoprefeitura
        fields = '__all__'

class LeicomplementarSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.Leicomplementar
        fields = '__all__'

class DocumentoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = models.Documento
        fields = '__all__'

class RegradocumentoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Regradocumento
        fields = '__all__'

class TipoarquivoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Tipoarquivo
        fields = '__all__'

class RegradocumentoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Regradocumento
        fields = '__all__'

class DeparacnaecodigoprefeituraSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Deparacnaecodigoprefeitura
        fields = '__all__'

class DeparacnaeleicomplementarSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Deparacnaeleicomplementar
        fields = '__all__'

class DeparaleicomplementarretencaoSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = models.Deparaleicomplementarretencao
        fields = '__all__'