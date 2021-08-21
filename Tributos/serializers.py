from rest_framework import serializers
from  tributos import models

class EsteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteira
        fields = '__all__'

class EsteiracampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteiracampo
        fields = '__all__'

class RegimeTributarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RegimeTributario
        fields = '__all__'

class EmpresaregimetributarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Empresaregimetributario
        fields = '__all__'

class ControletributosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Controletributos
        fields = '__all__'

class BlococampoconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blococampoconfig
        fields = '__all__'

class JurosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Juros
        fields = '__all__'

class MultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Multa
        fields = '__all__'

class EstornoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estorno
        fields = '__all__'

class TgcnfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tgcnfam
        fields = '__all__'

class TgcnfspSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tgcnfsp
        fields = '__all__'

class TgcnfstdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tgcnfstdm
        fields = '__all__'

class TgcnfstfmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tgcnfstfm
        fields = '__all__'

class TgcnfvmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tgcnfvm
        fields = '__all__'

class TributosBlococampoconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosBlococampoconfig
        fields = '__all__'

class TributosControletributosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosControletributos
        fields = '__all__'

class TributosEmpresaregimetributarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosEmpresaregimetributario
        fields = '__all__'

class TributosEsteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosEsteira
        fields = '__all__'

class TributosEsteiracampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosEsteiracampo
        fields = '__all__'

class TributosRegimetributarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TributosRegimetributario
        fields = '__all__'

class EsteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteira
        fields = '__all__'

class EsteiracampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteiracampo
        fields = '__all__'

class ObrigacaoacessoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Obrigacaoacessoria
        fields = '__all__'

class EsteirajurosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteirajuros
        fields = '__all__'

class EsteiramultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteiramulta
        fields = '__all__'

class EsteiraobrigacaoacessoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Esteiraobrigacaoacessoria
        fields = '__all__'

class ObrigacaoacessoriaObrigacaoacessoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ObrigacaoacessoriaObrigacaoacessoria
        fields = '__all__'