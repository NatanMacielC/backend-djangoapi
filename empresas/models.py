from django.db import models
from uuid import uuid4
from django.utils import timezone

# Create your models here.

# cadastro de empresas

class Empresa(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    CNPJ = models.CharField(max_length=20, null=False)

    DataAbertura = models.DateField(null=True)

    Bairro = models.CharField(max_length=150, null=True)

    Municipio = models.CharField(max_length=150, null=True)

    Estado =  models.CharField(max_length=2, null=True)

    RazaoSocial = models.CharField(max_length=250, null=True)

    Email = models.EmailField(max_length=150, null=True)

    NomeFantasia = models.CharField(max_length=250, null=True)

    Porte = models.CharField(max_length=100, null=True)

    Telefone = models.CharField(max_length=20, null=True)

    TelefoneAdicional = models.CharField(max_length=20, null=True)

    SituacaoCadastral = models.CharField(max_length=250, null=True)

    DataSituacaoCadastral = models.DateField(null=True)

    MotivoSituacaoCadastral = models.CharField(max_length=500, null=True)

    SituacaoEspecial = models.CharField(max_length=250, null=True)
    
    DataSituacaoEspecial = models.DateField(null=True)

    AtividadePrincipal = models.CharField(max_length=250, null=True)

    AtividadeSecundaria = models.CharField(max_length=250, null=True)

    Endereco = models.CharField(max_length=250, null=True)

    Numero = models.CharField(max_length=10, null=True)

    Complemento = models.CharField(max_length=150, null=True)

    Cep = models.CharField (max_length=10, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Empresa, self).save(*args, **kwargs)