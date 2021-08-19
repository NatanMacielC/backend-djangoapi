from django.db import models
from uuid import uuid4
from django.utils import timezone
from empresas.models import Empresa

# Create your models here.
    


class PlanoContasReferencial(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    Codigo = models.CharField(max_length=50, null=False)

    Descricao = models.CharField(max_length=150, null=False)

    DataCadastro = models.DateTimeField(editable=False)
    
    DataAlteracao= models.DateTimeField(null=True)

    Ativo = models.BooleanField(default=True, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(PlanoContasReferencial, self).save(*args, **kwargs)



# Plano Conta-Empresa
class EmpresaPlanoContas(models.Model):

    ID = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    EmpresaID = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=False)

    PlanoContasReferencialID = models.ForeignKey(PlanoContasReferencial, on_delete=models.CASCADE, null=False)




