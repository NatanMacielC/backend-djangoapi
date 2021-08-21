from rest_framework import viewsets
from tributos import serializers
from tributos import models

class RegimeTributarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegimeTributarioSerializer
    queryset = models.RegimeTributario.objects.all()

class EmpresaregimetributarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EmpresaregimetributarioSerializer
    queryset = models.Empresaregimetributario.objects.all()

class ControletributosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ControletributosSerializer
    queryset = models.Controletributos.objects.all()

class BlococampoconfigViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BlococampoconfigSerializer
    queryset = models.Blococampoconfig.objects.all()

class JurosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JurosSerializer
    queryset = models.Juros.objects.all()

class MultaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MultaSerializer
    queryset = models.Multa.objects.all()

class EstornoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EstornoSerializer
    queryset = models.Estorno.objects.all()

class EstornoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EstornoSerializer
    queryset = models.Estorno.objects.all()

class TgcnfspViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TgcnfspSerializer
    queryset = models.Tgcnfsp.objects.all()

class TgcnfstdmViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TgcnfstdmSerializer
    queryset = models.Tgcnfstdm.objects.all()

class TgcnfstfmViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TgcnfstfmSerializer
    queryset = models.Tgcnfstfm.objects.all()

class TgcnfvmViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TgcnfvmSerializer
    queryset = models.Tgcnfvm.objects.all()

class TgcnfamViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TgcnfamSerializer
    queryset = models.Tgcnfam.objects.all()

class TributosBlococampoconfigViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosBlococampoconfigSerializer
    queryset = models.TributosBlococampoconfig.objects.all()

class TributosControletributosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosControletributosSerializer
    queryset = models.TributosControletributos.objects.all()

class TributosEmpresaregimetributarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosEmpresaregimetributarioSerializer
    queryset = models.TributosEmpresaregimetributario.objects.all()

class TributosEsteiraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosEsteiraSerializer
    queryset = models.TributosEsteira.objects.all()

class TributosEsteiracampoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosEsteiracampoSerializer
    queryset = models.TributosEsteiracampo.objects.all()

class TributosRegimetributarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TributosRegimetributarioSerializer
    queryset = models.TributosRegimetributario.objects.all()

class EsteiraViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EsteiraSerializer
    queryset = models.Esteira.objects.all()

class EsteiracampoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EsteiracampoSerializer
    queryset = models.Esteiracampo.objects.all()

class ObrigacaoacessoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObrigacaoacessoriaSerializer
    queryset = models.Obrigacaoacessoria.objects.all()

class EsteirajurosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EsteirajurosSerializer
    queryset = models.Esteirajuros.objects.all()

class EsteiramultaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EsteiramultaSerializer
    queryset = models.Esteiramulta.objects.all()

class EsteiraobrigacaoacessoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EsteiraobrigacaoacessoriaSerializer
    queryset = models.Esteiraobrigacaoacessoria.objects.all()

class ObrigacaoacessoriaObrigacaoacessoriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObrigacaoacessoriaObrigacaoacessoriaSerializer
    queryset = models.ObrigacaoacessoriaObrigacaoacessoria.objects.all()