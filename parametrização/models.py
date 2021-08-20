from ObrigacaoAcessoria.models import ObrigacaoAcessoria
from django.db import models
from django.utils import timezone

# Create your models here.
    
# cadastro das regras
class Regra(models.Model):

    ID = models.AutoField(primary_key=True, editable=False)

    Codigo = models.CharField(max_length=50, null=False)

    Nome = models.CharField(max_length=100, null=True)

    Descricao = models.CharField(max_length=150, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.ID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Regra, self).save(*args, **kwargs)



# cadastro dos eventos
class Evento(models.Model):

    ID = models.AutoField(primary_key=True, editable=False)

    Nome = models.CharField(max_length=100, null=True)
    
    # FiscoID = models.ForeignKey(Fisco, on_delete=models.CASCADE, null=False)

    # GeracaoCreditoID = models.ForeignKey(Fisco, on_delete=models.CASCADE, null=False)

    # RetencaoFonteID = models.ForeignKey(Fisco, on_delete=models.CASCADE, null=False)

    # PeriodicidadeID = models.ForeignKey(Fisco, on_delete=models.CASCADE, null=False)

    ObrigacaoAcessorialID = models.ForeignKey(ObrigacaoAcessoria, on_delete=models.CASCADE, null=False)

    ContaReferecial = models.CharField(max_length=20, null=True)

    DescContaReferencial = models.CharField(max_length=150, null=True)

    Aliquota = models.DecimalField(max_digits=38, decimal_places=38, null=True)

    RegimeTributario = models.CharField(max_length=50, null=True)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField()

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.ID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Evento, self).save(*args, **kwargs)



# execução da parametrização
class Parametrizacao(models.Model):

    ID = models.AutoField(primary_key=True, editable=False)

    EventoID = models.ForeignKey(Evento, on_delete=models.CASCADE, null=False)

    Nome = models.CharField(max_length=50, null=True)
    
    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField()

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.ID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Parametrizacao, self).save(*args, **kwargs)


# a parametrização regra
class ParametrizacaoRegra(models.Model):

    ID = models.AutoField(primary_key=True, editable=False)

    ParametrizacaoID = models.ForeignKey(Parametrizacao, on_delete=models.CASCADE, null=False)

    RegraID = models.ForeignKey(Regra, on_delete=models.CASCADE, null=False)
