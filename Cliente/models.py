from django.db import models

    
class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nomefantasia = models.CharField(db_column='NomeFantasia', max_length=250, blank=True, null=True)  
    cnpj = models.CharField(db_column='CNPJ', max_length=20, blank=True, null=True)  
    razaosocial = models.CharField(db_column='RazaoSocial', max_length=350, blank=True, null=True)  
    dataabertura = models.DateTimeField(db_column='DataAbertura', blank=True, null=True)  
    porte = models.CharField(db_column='Porte', max_length=100, blank=True, null=True)  
    atividadeprincipal = models.CharField(db_column='AtividadePrincipal', max_length=250, blank=True, null=True)  
    atividadesecundaria = models.CharField(db_column='AtividadeSecundaria', max_length=250, blank=True, null=True)  
    endereco = models.CharField(db_column='Endereco', max_length=250, blank=True, null=True)  
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True)  
    complemento = models.CharField(db_column='Complemento', max_length=150, blank=True, null=True)  
    bairro = models.CharField(db_column='Bairro', max_length=150, blank=True, null=True)  
    cidade = models.CharField(db_column='Cidade', max_length=150, blank=True, null=True)  
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  
    cep = models.CharField(db_column='CEP', max_length=10, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=250, blank=True, null=True) 
    telefone = models.CharField(db_column='Telefone', max_length=20, blank=True, null=True)  
    telefoneadicional = models.CharField(db_column='TelefoneAdicional', max_length=20, blank=True, null=True)  
    situacaocadastral = models.CharField(db_column='SituacaoCadastral', max_length=250, blank=True, null=True)  
    datasituacaocadastral = models.DateTimeField(db_column='DataSituacaoCadastral', blank=True, null=True)  
    motivosituacaocadastral = models.CharField(db_column='MotivoSituacaoCadastral', max_length=500, blank=True, null=True)  
    situacaoespecial = models.CharField(db_column='SituacaoEspecial', max_length=250, blank=True, null=True)  
    datasituacaoespecial = models.DateTimeField(db_column='DataSituacaoEspecial', blank=True, null=True)  
    clientedesde = models.DateTimeField(db_column='ClienteDesde', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now= True, blank=True, null=True) 
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True) 
    inscricaoestadual = models.CharField(db_column='InscricaoEstadual', max_length=20, blank=True, null=True) 
    codigomunicipio = models.CharField(db_column='CodigoMunicipio', max_length=20, blank=True, null=True)  
    inscricaomunicipal = models.CharField(db_column='InscricaoMunicipal', max_length=20, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Cliente'



class ClienteCliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nomefantasia = models.CharField(db_column='NomeFantasia', max_length=250, blank=True, null=True)  
    cnpj = models.CharField(db_column='CNPJ', max_length=20, blank=True, null=True)  
    razaosocial = models.CharField(db_column='RazaoSocial', max_length=350, blank=True, null=True)  
    dataabertura = models.DateField(db_column='DataAbertura', blank=True, null=True)  
    porte = models.CharField(db_column='Porte', max_length=100, blank=True, null=True)  
    atividadeprincipal = models.CharField(db_column='AtividadePrincipal', max_length=250, blank=True, null=True)  
    atividadesecundaria = models.CharField(db_column='AtividadeSecundaria', max_length=250, blank=True, null=True)  
    endereco = models.CharField(db_column='Endereco', max_length=250, blank=True, null=True)  
    numero = models.CharField(db_column='Numero', max_length=10, blank=True, null=True)  
    complemento = models.CharField(db_column='Complemento', max_length=150, blank=True, null=True)  
    bairro = models.CharField(db_column='Bairro', max_length=250, blank=True, null=True)  
    cidade = models.CharField(db_column='Cidade', max_length=150, blank=True, null=True)  
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  
    cep = models.CharField(db_column='CEP', max_length=10, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=250, blank=True, null=True)  
    telefone = models.CharField(db_column='Telefone', max_length=20, blank=True, null=True)  
    telefoneadicional = models.CharField(db_column='TelefoneAdicional', max_length=20, blank=True, null=True)  
    situacaocadastral = models.CharField(db_column='SituacaoCadastral', max_length=250, blank=True, null=True)  
    datasituacaocadastral = models.DateField(db_column='DataSituacaoCadastral', blank=True, null=True)  
    motivosituacaocadastral = models.CharField(db_column='MotivoSituacaoCadastral', max_length=500, blank=True, null=True)  
    situacaoespecial = models.CharField(db_column='SituacaoEspecial', max_length=250, blank=True, null=True)  
    datasituacaoespecial = models.DateField(db_column='DataSituacaoEspecial', blank=True, null=True)  
    clientedesde = models.DateField(db_column='ClienteDesde', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now= True, blank=True, null=True) 
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True) 
    inscricaoestadual = models.CharField(db_column='InscricaoEstadual', max_length=20, blank=True, null=True)  
    codigomunicipio = models.CharField(db_column='CodigoMunicipio', max_length=20, blank=True, null=True)  
    inscricaomunicipal = models.CharField(db_column='InscricaoMunicipal', max_length=20, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Cliente_cliente'


class ClienteClienteempresa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    clienteid_id = models.IntegerField(db_column='ClienteID_id')  
    empresaid_id = models.IntegerField(db_column='EmpresaID_id')  

    class Meta:
        managed = False
        db_table = 'Cliente_clienteempresa'



class Grupo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=100)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    clienteid = models.ForeignKey(Cliente, on_delete=models.CASCADE, db_column='ClienteID')  

    class Meta:
        managed = False
        db_table = 'Grupo'
