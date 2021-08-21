from django.db import models
from cliente.models import Cliente, Grupo
from planocontas.models import Planocontasreferencial

# Create your models here.

# cadastro de empresa

class Empresa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    cnpj = models.CharField(db_column='CNPJ', max_length=20)  
    dataabertura = models.DateTimeField(db_column='DataAbertura', blank=True, null=True)  
    bairro = models.CharField(db_column='Bairro', max_length=150, blank=True, null=True)  
    municipio = models.CharField(db_column='Municipio', max_length=150, blank=True, null=True)  
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  
    razaosocial = models.CharField(db_column='RazaoSocial', max_length=250, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=150, blank=True, null=True)  
    nomefantasia = models.CharField(db_column='NomeFantasia', max_length=250, blank=True, null=True)  
    porte = models.CharField(db_column='Porte', max_length=100, blank=True, null=True)  
    telefone = models.CharField(db_column='Telefone', max_length=20, blank=True, null=True)  
    telefoneadicional = models.CharField(db_column='TelefoneAdicional', max_length=20, blank=True, null=True)  
    situacaocadastral = models.CharField(db_column='SituacaoCadastral', max_length=250, blank=True, null=True) 
    datasituacaocadastral = models.DateTimeField(db_column='DataSituacaoCadastral', blank=True, null=True)  
    motivosituacaocadastral = models.CharField(db_column='MotivoSituacaoCadastral', max_length=500, blank=True, null=True) 
    situacaoespecial = models.CharField(db_column='SituacaoEspecial', max_length=250, blank=True, null=True)  
    datasituacaoespecial = models.DateTimeField(db_column='DataSituacaoEspecial', blank=True, null=True)  
    atividadeprincipal = models.CharField(db_column='AtividadePrincipal', max_length=250, blank=True, null=True)  
    atividadesecundaria = models.CharField(db_column='AtividadeSecundaria', max_length=250, blank=True, null=True)  
    endereco = models.CharField(db_column='Endereco', max_length=250, blank=True, null=True)  
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True) 
    complemento = models.CharField(db_column='Complemento', max_length=150, blank=True, null=True)  
    cep = models.CharField(db_column='Cep', max_length=10, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True) 
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Empresa' 



class Grupoempresa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  
    grupoid = models.ForeignKey(Grupo, on_delete=models.CASCADE, db_column='GrupoID')  

    class Meta:
        managed = False
        db_table = 'GrupoEmpresa'



class Fornecedor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    cnpj = models.CharField(db_column='CNPJ', max_length=20)  
    cnae = models.CharField(db_column='CNAE', max_length=20, blank=True, null=True)  
    codigoservico = models.CharField(db_column='CodigoServico', max_length=50, blank=True, null=True)  
    descricaoservico = models.CharField(db_column='DescricaoServico', max_length=150, blank=True, null=True)  
    tipofornecedor = models.CharField(db_column='TipoFornecedor', max_length=50, blank=True, null=True)  
    servicotomado = models.CharField(db_column='ServicoTomado', max_length=50, blank=True, null=True)  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Fornecedor'



class Empresaplanocontas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  
    planocontasreferencialid = models.ForeignKey(Planocontasreferencial, on_delete=models.CASCADE, db_column='PlanoContasReferencialID')  

    class Meta:
        managed = False
        db_table = 'EmpresaPlanoContas'



class PlanocontasEmpresaplanocontas(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    empresaid_id = models.CharField(db_column='EmpresaID_id', max_length=32)  
    planocontasreferencialid_id = models.CharField(db_column='PlanoContasReferencialID_id', max_length=32)  

    class Meta:
        managed = False
        db_table = 'PlanoContas_empresaplanocontas'

class Clienteempresa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='ClienteID')  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  

    class Meta:
        managed = False
        db_table = 'ClienteEmpresa'