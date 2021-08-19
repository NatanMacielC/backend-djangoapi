from django.db import models
from uuid import uuid4
from django.db.models.deletion import CASCADE
from django.utils import timezone
from empresas.models import Empresa

# Create your models here.
    


class RegimeTributario(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    Nome = models.CharField(max_length=50, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(RegimeTributario, self).save(*args, **kwargs)



# Empresa-RegimeTributario
class EmpresaRegimeTributario(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    EmpresaID = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False)

    RegimeTributarioID = models.ForeignKey(RegimeTributario, on_delete=models.CASCADE, null=False)



 # Esteira
class Esteira(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    EmpresaID = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False)

    RegimeTributarioID = models.ForeignKey(RegimeTributario, on_delete=models.CASCADE, null=False)



# Controle de Tributos
class ControleTributos(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    CodigoContabil = models.CharField(max_length=50, null=True)

    DescricaoCodigoContabil = models.CharField(max_length=150, null=True)

    MesCompetencia = models.IntegerField(null=True)

    AnoCompetencia = models.IntegerField(null=True)

    ValorProvisaoRecolher = models.DecimalField(max_digits=38, decimal_places=38, null=True)

    TipoLancamentoPrevisao = models.CharField(max_length=50, null=True)

    Historico = models.CharField(max_length=250, null=True)

    Vencimento = models.DateField(null=True)

    DataRecolhimento = models.DateField(null=True)

    ValorRecolhimento = models.DecimalField(max_digits=38, decimal_places=38, null=True)

    TipoLancamento = models.CharField(max_length=50, null=True)

    Status = models.CharField(max_length=50, null=True)

    MensagemAviso = models.CharField(max_length=250, null=True)

    MensagemRecomendacao = models.CharField(max_length=250, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(RegimeTributario, self).save(*args, **kwargs)

    EsteiraID = models.ForeignKey(Esteira, on_delete=models.CASCADE, null=False)



# Bloco-Campo Config
class BlocoCampoConfig(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    Bloco = models.CharField(max_length=50, null=True)

    Campo = models.CharField(max_length=50, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(RegimeTributario, self).save(*args, **kwargs)



# Esteira-Campo
class EsteiraCampo(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    EsteiraID = models.ForeignKey(Esteira, on_delete=models.CASCADE, null=False)

    BlocoCampoConfig = models.ForeignKey(BlocoCampoConfig, on_delete=models.CASCADE, null=False)

    Valor = models.DecimalField(max_digits=38, decimal_places=38, null=True)
