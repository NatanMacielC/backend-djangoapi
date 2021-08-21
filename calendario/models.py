from django.db import models

# Create your models here.



# cadastro dos calendários
class Calendario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    nomecalendario = models.CharField(db_column='NomeCalendario', max_length=150, blank=True, null=True)  
    tipo = models.CharField(db_column='Tipo', max_length=50, blank=True, null=True)  
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  
    municipio = models.CharField(db_column='Municipio', max_length=150, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True) 

    def __str__(self):
        return self.tipo + ' - ' + self.nomecalendario

    class Meta:
        managed = False
        db_table = 'Calendario'


# cadastro dos feriados    
class Calendarioferiado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    calendarioid = models.ForeignKey(Calendario, on_delete=models.CASCADE, db_column='CalendarioID')  
    ano = models.IntegerField(db_column='Ano', blank=True, null=True)  
    mes = models.IntegerField(db_column='Mes', blank=True, null=True)  
    dia = models.IntegerField(db_column='Dia', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  

    def __str__(self):
            return self.dia +  '/' + self.mes + '/'+ self.ano + '/' + self.descricao

    class Meta:
        managed = False
        db_table = 'CalendarioFeriado'
    

    
