from django.db import models
from django.utils import timezone 


class Planocontasreferencial(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=50)  
    descricao = models.CharField(db_column='Descricao', max_length=150)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  

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




