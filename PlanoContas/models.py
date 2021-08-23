from django.db import models
from django.utils import timezone 


class Planocontasreferencial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=50)  
    descricao = models.CharField(db_column='Descricao', max_length=150)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)
    versao = models.CharField(db_column='Versao', max_length=20, blank=True, null=True) 
    datavalidade = models.DateField(db_column='DataValidade', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PlanoContasReferencial'



class PlanocontasPlanocontasreferencial(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    codigo = models.CharField(db_column='Codigo', max_length=50)  
    descricao = models.CharField(db_column='Descricao', max_length=150)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True)  

    class Meta:
        managed = False
        db_table = 'PlanoContas_planocontasreferencial'

class Planocontasitem(models.Model):
        id = models.AutoField(db_column='ID', primary_key=True)  
        planocontasrefencialid = models.ForeignKey(Planocontasreferencial, on_delete=models.CASCADE, db_column='PlanoContasReferencialID')    
        codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)
        datainicio = models.DateField(db_column='DataInicio', blank=True, null=True)
        datafim = models.DateField(db_column='DataFim', blank=True, null=True)   
        tipo = models.CharField(db_column='Tipo', max_length=1, blank=True, null=True)
        contasuperior = models.CharField(db_column='ContaSuperior', max_length=50, blank=True, null=True)
        nivel = models.IntegerField(db_column='Nivel', blank=True, null=True) 
        natureza = models.IntegerField(db_column='Natureza', blank=True, null=True) 
        orientacoes = models.CharField(db_column='Orientacoes', max_length=500, blank=True, null=True)
        datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
        dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
        ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)   






