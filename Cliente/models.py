from django.db import models
from django.utils import timezone
from empresas.models import Empresa

# Create your models here.
    


class Cliente(models.Model):

    ID = models.AutoField(primary_key=True, editable=False, null=False)

    NomeFantasia = models.CharField(max_length=250, null=True)

    CNPJ = models.CharField(max_length=20, null=True)

    RazaoSocial = models.CharField(max_length=350, null=True)

    DataAbertura= models.DateField(null=True)

    Porte = models.CharField(max_length=100, null=True)

    AtividadePrincipal = models.CharField(max_length=250, null=True)

    AtividadeSecundaria = models.CharField(max_length=250, null=True)

    Endereco = models.CharField(max_length=250, null=True)

    Numero = models.CharField(max_length=10, null=True)

    Complemento = models.CharField(max_length=150, null=True)

    Bairro = models.CharField(max_length=250, null=True)

    Cidade = models.CharField(max_length=150, null=True)

    Estado = models.CharField(max_length=2, null=True)

    CEP = models.CharField(max_length=10, null=True)

    Email = models.EmailField(max_length=250, null=True)

    Telefone = models.CharField(max_length=20, null=True)

    TelefoneAdicional = models.CharField(max_length=20, null=True)

    SituacaoCadastral = models.CharField(max_length=250, null=True)

    DataSituacaoCadastral = models.DateField(null=True)

    MotivoSituacaoCadastral = models.CharField(max_length=500, null=True)

    SituacaoEspecial = models.CharField(max_length=250, null=True)

    DataSituacaoEspecial = models.DateField(null=True)

    ClienteDesde = models.DateField(null=True)

    DataCadastro = models.DateTimeField(editable=False, null=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    InscricaoEstadual = models.CharField(max_length=20, null=True)

    CodigoMunicipio = models.CharField(max_length=20, null=True)

    InscricaoMunicipal = models.CharField(max_length=20, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.ID:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Cliente, self).save(*args, **kwargs)



class ClienteEmpresa(models.Model):

    ID = models.AutoField(primary_key=True, editable=False, null=False)

    ClienteID = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)

    EmpresaID = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False)




