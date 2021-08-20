from django.db import models
from Tributos.models import BlocoCampoConfig
from django.utils import timezone

# Create your models here.

# model das Obrigações Acessórias 

class ObrigacaoAcessoria(models.Model):

    ID = models.AutoField(primary_key=True, editable=False)

    Versao = models.CharField(max_length=20, null=True)

    Bloco = models.CharField(max_length=20, null=True)

    Campo = models.CharField(max_length=20, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    BlocoCampoConfigID = models.ForeignKey(BlocoCampoConfig, on_delete=models.CASCADE, null=False)

    Escopo = models.CharField(max_length=50, null=False)

    PosicaoTXT = models.CharField(max_length=20, null=True)

    Tamanho = models.CharField(max_length=20, null=True)

    PaginaManual = models.CharField(max_length=100, null=True)

    Observacao = models.CharField(max_length=250, null=True)

    Registro = models.CharField(max_length=150, null=True)

    OrdemClassificacao = models.CharField(max_length=20, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.ID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(ObrigacaoAcessoria, self).save(*args, **kwargs)