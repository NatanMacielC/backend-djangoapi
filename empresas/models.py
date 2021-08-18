from django.db import models
from uuid import uuid4
from django_cpf_cnpj.fields import CPFField, CNPJField
from django.core.validators import RegexValidator


# Create your models here.

#cadastro de empresas
class Empresas(models.Model):

    id_empresa = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    razao_social = models.CharField(max_length=80)
    nome_fantasia = models.CharField(max_length=80)
    porte = models.CharField(max_length=100)
    cnpj = CNPJField(masked=True, null=False, blank=False)
    descricao_principal = models.CharField(max_length=100)
    descricao_secundaria = models.CharField(max_length=100)
    release_date = models.DateField(null=False, blank=False)
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=50)
    estado = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    adPhoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    email = models.EmailField(max_length=100)


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


    uf = models.CharField (max_length=2, choices=UF_CHOICES, blank=False, null=False)
    situacao_cadastral = models.CharField (max_length=250)
    data_situacao_cadastral = models.DateField(null=False, blank=False)
    motivo_situacao_cadastral = models.CharField (max_length=250)
    situacao_especial = models.CharField (max_length=250)
    data_situacao_especial = models.DateField (null=False, blank=False)
    create_at =  models.DateField(auto_now_add=True)
