from django.db import models

# Create your models here.


# cadastro dos feriados    
class FeriadoCalendario(models.Model):
    dataFeriado = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return "%s %s" % (self.dataFeriado, self.descricao)


# cadastro dos calendários
class Calendario(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    tipo = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    municipio = models.CharField(max_length=100)
    feriado = models.ForeignKey(FeriadoCalendario, on_delete=models.CASCADE)
    def __str__(self):
            return self.tipo

    class Meta:
        ordering = ['tipo']

    
