from calendario import models
from rest_framework import viewsets, serializers
from parametrização.models import Documento, Cnae, Codigoprefeitura, Deparacnaecodigoprefeitura, Deparacnaeleicomplementar, Deparaleicomplementarretencao, Evento, Eventogrupo, Geracaocredito, Grupoevento, Leicomplementar, Parametrizacao, Parametrizacaoregra, Periodicidade, Regra, Regradocumento, Retencaofonte, Tipoarquivo
from parametrização import serializers

# Create your views here.
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = serializers.EventoSerializer

class RegrasViewSet(viewsets.ModelViewSet):
    queryset = Regra.objects.all()
    serializer_class = serializers.RegraSerializer

class CnaeViewSet(viewsets.ModelViewSet):
    queryset = Cnae.objects.all()
    serializer_class = serializers.CnaeSerializer

class GeracaocreditoViewSet(viewsets.ModelViewSet):
    queryset = Geracaocredito.objects.all()
    serializer_class = serializers.GeracaocreditoSerializer

class RetencaofonteViewSet(viewsets.ModelViewSet):
    queryset = Retencaofonte.objects.all()
    serializer_class = serializers.RetencaofonteSerializer

class PeriodicidadeViewSet(viewsets.ModelViewSet):
    queryset = Periodicidade.objects.all()
    serializer_class = serializers.PeriodicidadeSerializer

class GrupoeventoViewSet(viewsets.ModelViewSet):
    queryset = Grupoevento.objects.all()
    serializer_class = serializers.GrupoeventoSerializer

class EventogrupoViewSet(viewsets.ModelViewSet):
    queryset = Eventogrupo.objects.all()
    serializer_class = serializers.EventogrupoSerializer

class ParametrizacaoViewSet(viewsets.ModelViewSet):
    queryset = Parametrizacao.objects.all()
    serializer_class = serializers.ParametrizacaoSerializer

class ParametrizacaoregraViewSet(viewsets.ModelViewSet):
    queryset = Parametrizacaoregra.objects.all()
    serializer_class = serializers.ParametrizacaoregraSerializer

class CodigoprefeituraViewSet(viewsets.ModelViewSet):
    queryset = Codigoprefeitura.objects.all()
    serializer_class = serializers.CodigoprefeituraSerializer

class LeicomplementarViewSet(viewsets.ModelViewSet):
    queryset = Leicomplementar.objects.all()
    serializer_class = serializers.LeicomplementarSerializer

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = serializers.DocumentoSerializer

class RegradocumentoViewSet(viewsets.ModelViewSet):
    queryset = Regradocumento.objects.all()
    serializer_class = serializers.RegradocumentoSerializer

class TipoarquivoViewSet(viewsets.ModelViewSet):
    queryset = Tipoarquivo.objects.all()
    serializer_class = serializers.TipoarquivoSerializer

class DeparacnaecodigoprefeituraViewSet(viewsets.ModelViewSet):
    queryset = Deparacnaecodigoprefeitura.objects.all()
    serializer_class = serializers.DeparacnaecodigoprefeituraSerializer

class DeparacnaeleicomplementarViewSet(viewsets.ModelViewSet):
    queryset = Deparacnaeleicomplementar.objects.all()
    serializer_class = serializers.DeparacnaeleicomplementarSerializer

class DeparaleicomplementarretencaoViewSet(viewsets.ModelViewSet):
    queryset = Deparaleicomplementarretencao.objects.all()
    serializer_class = serializers.DeparaleicomplementarretencaoSerializer