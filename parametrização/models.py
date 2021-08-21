from django.db import models
from fisco.models import Fisco
from tributos.models import Obrigacaoacessoria

# Create your models here.

class Cnae(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=20, blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Cnae'



class Geracaocredito(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'GeracaoCredito'


class Regra(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  
    nome = models.CharField(db_column='Nome', max_length=100, blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Regra'



class Retencaofonte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=20, blank=True, null=True)  
    aliquota = models.CharField(db_column='Aliquota', max_length=20, blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'Retencaofonte'



class Periodicidade(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Periodicidade'



class Evento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=100, blank=True, null=True)  
    fiscoid = models.ForeignKey(Fisco, on_delete=models.CASCADE, db_column='FiscoID')  
    geracaocreditoid = models.ForeignKey(Geracaocredito, on_delete=models.CASCADE, db_column='GeracaoCreditoID')  
    retencaofonteid = models.ForeignKey(Retencaofonte, on_delete=models.CASCADE, db_column='RetencaoFonteID')  
    periodicidadeid = models.ForeignKey(Periodicidade, on_delete=models.CASCADE, db_column='PeriodicidadeID')  
    obrigacaoacessoriaid = models.ForeignKey(Obrigacaoacessoria, on_delete=models.CASCADE, db_column='ObrigacaoAcessoriaID')  
    contareferencial = models.CharField(db_column='ContaReferencial', max_length=20, blank=True, null=True)  
    desccontareferencial = models.CharField(db_column='DescContaReferencial', max_length=150, blank=True, null=True)  
    aliquota = models.DecimalField(db_column='Aliquota', max_digits=38, decimal_places=0, blank=True, null=True)  
    regimetributario = models.CharField(db_column='RegimeTributario', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Evento'



class Grupoevento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'GrupoEvento'



class Eventogrupo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    eventoid = models.ForeignKey(Evento, on_delete=models.CASCADE, db_column='EventoID')  
    grupoeventoid = models.ForeignKey(Grupoevento, on_delete=models.CASCADE, db_column='GrupoEventoID')  

    class Meta:
        managed = False
        db_table = 'EventoGrupo'



class Parametrizacao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    eventoid = models.ForeignKey(Evento, on_delete=models.CASCADE, db_column='EventoID')  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Parametrizacao'


class Parametrizacaoregra(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    parametrizacaoid = models.ForeignKey(Parametrizacao, on_delete=models.CASCADE, db_column='ParametrizacaoID')  
    regraid = models.ForeignKey(Regra, on_delete=models.CASCADE, db_column='RegraID')  

    class Meta:
        managed = False
        db_table = 'ParametrizacaoRegra'



class Codigoprefeitura(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigoibge = models.CharField(db_column='CodigoIBGE', max_length=20, blank=True, null=True)  
    descricaoprefeitura = models.CharField(db_column='DescricaoPrefeitura', max_length=150, blank=True, null=True)  
    codigoservico = models.CharField(db_column='CodigoServico', max_length=20, blank=True, null=True)  
    descricaoservico = models.CharField(db_column='DescricaoServico', max_length=100, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'CodigoPrefeitura'





class Leicomplementar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigo = models.CharField(db_column='Codigo', max_length=20, blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'LeiComplementar'



class Documento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    xml = models.BooleanField(blank=True, null=True)
    txt = models.BooleanField(blank=True, null=True)
    pdf = models.BooleanField(blank=True, null=True)
    doc = models.BooleanField(blank=True, null=True)
    xls = models.BooleanField(blank=True, null=True)
    ofx = models.BooleanField(blank=True, null=True)
    csv = models.BooleanField(blank=True, null=True)
    json = models.BooleanField(blank=True, null=True)
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    xlsx = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Documento'



class Regradocumento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    regraid = models.ForeignKey(Regra, on_delete=models.CASCADE, db_column='RegraID', blank=True, null=True)  
    documentoid = models.ForeignKey(Documento, on_delete=models.CASCADE, db_column='DocumentoID', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'RegraDocumento'


class Tipoarquivo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TipoArquivo'


class Deparacnaecodigoprefeitura(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    cnaeid = models.ForeignKey(Cnae, on_delete=models.CASCADE, db_column='CnaeID')  
    codigoprefeituraid = models.ForeignKey(Codigoprefeitura, on_delete=models.CASCADE, db_column='CodigoPrefeituraID')  

    class Meta:
        managed = False
        db_table = 'DeParaCnaeCodigoPrefeitura'



class Deparacnaeleicomplementar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    cnaeid = models.ForeignKey(Cnae, on_delete=models.CASCADE, db_column='CnaeID')  
    leicomplementarid = models.ForeignKey(Leicomplementar, on_delete=models.CASCADE, db_column='LeiComplementarID')  

    class Meta:
        managed = False
        db_table = 'DeParaCnaeLeiComplementar'



class Deparaleicomplementarretencao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    leicomplementarid = models.ForeignKey(Leicomplementar, on_delete=models.CASCADE, db_column='LeiComplementarID')  
    retencaofonteid = models.ForeignKey(Retencaofonte, on_delete=models.CASCADE, db_column='RetencaoFonteID')  

    class Meta:
        managed = False
        db_table = 'DeParaLeiComplementarRetencao'