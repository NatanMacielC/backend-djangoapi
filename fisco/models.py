from django.db import models
from uuid import uuid4

# Create your models here.
class Fisco(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=50)

    RONDONIA = 'RO'
    ACRE = 'AC'
    AMAZONAS = 'AM'
    RORAIMA = 'RR'
    PARA = 'PA'
    AMAPA = 'AP'
    TOCANTINS = 'TO'
    MARANHAO = 'MA'
    PIAUI = 'PI'
    CEARA = 'CE'
    RIO_GRANDE_DO_NORTE = 'RN'
    PARAIBA = 'PB'
    PERNAMBUCO = 'PE'
    ALAGOAS = 'AL'
    SERGIPE = 'SE'
    BAHIA = 'BA'
    MINAS_GERAIS = 'MG'
    ESPIRITO_SANTO = 'ES'
    RIO_DE_JANEIRO = 'RJ'
    SAO_PAULO = 'SP'
    PARANA = 'PR'
    SANTA_CATARINA = 'SC'
    RIO_GRANDE_DO_SUL = 'RS'
    MATO_GROSSO_DO_SUL = 'MS'
    MATO_GROSSO = 'MT'
    GOIAS = 'GO'
    DISTRITO_FEDERAL = 'DF'
    UF_CHOICES = (
        (RONDONIA, "Rondônia"),
        (ACRE, "Acre"),
        (AMAZONAS, "Amazonas"),
        (RORAIMA, "Roraima"),
        (PARA, "Pará"),
        (AMAPA, "Amapá"),
        (TOCANTINS, "Tocantins"),
        (MARANHAO, "Maranhão"),
        (PIAUI, "Piauí"),
        (CEARA, "Ceará"),
        (RIO_GRANDE_DO_NORTE, "Rio Grande do Norte"),
        (PARAIBA, "Paraíba"),
        (PERNAMBUCO, "Pernambuco"),
        (ALAGOAS, "Alagoas"),
        (SERGIPE, "Sergipe"),
        (BAHIA, "Bahia"),
        (MINAS_GERAIS, "Minas Gerais"),
        (ESPIRITO_SANTO, "Espírito Santo"),
        (RIO_DE_JANEIRO, "Rio de Janeiro"),
        (SAO_PAULO, "São Paulo"),
        (PARANA, "Paraná"),
        (SANTA_CATARINA, "Santa Catarina"),
        (RIO_GRANDE_DO_SUL, "Rio Grande do Sul"),
        (MATO_GROSSO_DO_SUL, "Mato Grosso do Sul"),
        (MATO_GROSSO, "Mato Grosso"),
        (GOIAS, "Goiás"),
        (DISTRITO_FEDERAL, "Distrito Federal"),
    )

    estado = models.CharField(max_length=2, choices=UF_CHOICES, blank=False, null=False)
    municipio = models.CharField(max_length=150)
    vencimento = models.DateField()

    class Regras(models.IntegerChoices):
        PROXIMO = 0, 'Próximo dia útil'
        ANTERIOR = 1, 'Dia útil anterior'

    regraTributo = models.IntegerField(choices=Regras.choices)
    dataCadastro = models.DateField(auto_now_add=True)
    dataAlteracao = models.DateField()
    ativo = models.BooleanField(default=True)
    def __str__(self):
            return self.nome, self.estado, self.municipio, self.vencimento, self.regraTributo, self.dataCadastro, self.dataAlteracao, self.ativo

    class Meta:
        ordering = ['nome', 'estado', 'municipio', 'vencimento', 'regraTributo', 'dataCadastro', 'dataAlteracao', 'ativo']





