from django.db import models
from uuid import uuid4

# Create your models here.
    
class FeriadoCalendario(models.Model):
    dataFeriado = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s" % (self.dataFeriado, self.descricao)


class Calendario(models.Model):
    id_calendario = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    tipo = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    municipio = models.CharField(max_length=100)
    feriado = models.ForeignKey(FeriadoCalendario, on_delete=models.CASCADE)
    def __str__(self):
            return self.tipo

    class Meta:
        ordering = ['tipo']

    
