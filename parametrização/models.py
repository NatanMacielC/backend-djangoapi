from django.db import models

# Create your models here.
from django.db import models
from uuid import uuid4

# Create your models here.
    
# cadastro das regras
class Regras(models.Model):
    id_regra = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    regra = models.CharField(max_length=250, null=False, blank=False)
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s" % (self.regra, self.tipo)


# cadastro dos eventos
class Evento(models.Model):
    id_Evento = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=250, null=True, blank=True)
    parametrizacao = models.ForeignKey(Regras, on_delete=models.CASCADE)
    def __str__(self):
            return self.tipo, self.descricao, self.parametrizacao

    class Meta:
        ordering = ['tipo', 'descricao', 'parametrizacao']

    
