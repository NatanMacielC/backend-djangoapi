from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from empresa.models import Empresa
from fisco.models import Fisco
from usuario.models import Usuario

# Create your models here.
    


class RegimeTributario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True,blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'RegimeTributario'


class Esteira(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  
    regimetributarioid = models.ForeignKey(RegimeTributario, on_delete=models.CASCADE, db_column='RegimeTributarioID')  

    class Meta:
        managed = False
        db_table = 'Esteira'



class Empresaregimetributario(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    empresaid = models.ForeignKey(Empresa, on_delete=models.CASCADE, db_column='EmpresaID')  
    regimetributarioid = models.ForeignKey(RegimeTributario, on_delete=models.CASCADE, db_column='RegimeTributarioID')  

    class Meta:
        managed = False
        db_table = 'EmpresaRegimeTributario'




class Controletributos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    codigocontabil = models.CharField(db_column='CodigoContabil', max_length=50, blank=True, null=True)  
    descricaocodigocontabil = models.CharField(db_column='DescricaoCodigoContabil', max_length=150, blank=True, null=True)  
    mescompetencia = models.IntegerField(db_column='MesCompetencia', blank=True, null=True)  
    anocompetencia = models.IntegerField(db_column='AnoCompetencia', blank=True, null=True)  
    valorprovisaorecolher = models.DecimalField(db_column='ValorProvisaoRecolher', max_digits=38, decimal_places=0, blank=True, null=True)  
    tipolancamentoprevisao = models.CharField(db_column='TipoLancamentoPrevisao', max_length=50, blank=True, null=True)  
    historico = models.CharField(db_column='Historico', max_length=250, blank=True, null=True)  
    vencimento = models.DateTimeField(db_column='Vencimento', blank=True, null=True)  
    datarecolhimento = models.DateTimeField(db_column='DataRecolhimento', blank=True, null=True)  
    valorrecolhimento = models.DecimalField(db_column='ValorRecolhimento', max_digits=38, decimal_places=0, blank=True, null=True)  
    tipolancamento = models.CharField(db_column='TipoLancamento', max_length=50, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  
    mensagemaviso = models.CharField(db_column='MensagemAviso', max_length=250, blank=True, null=True)  
    mensagemrecomendacao = models.CharField(db_column='MensagemRecomendacao', max_length=250, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  

    class Meta:
        managed = False
        db_table = 'ControleTributos'



class Blococampoconfig(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    bloco = models.CharField(db_column='Bloco', max_length=50, blank=True, null=True)  
    campo = models.CharField(db_column='Campo', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'BlocoCampoConfig'



class Esteiracampo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    blococampoconfigid = models.ForeignKey(Blococampoconfig, on_delete=models.CASCADE, db_column='BlocoCampoConfigID')  
    valor = models.DecimalField(db_column='Valor', max_digits=38, decimal_places=0, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'EsteiraCampo'


class Juros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    valor = models.DecimalField(db_column='Valor', max_digits=38, decimal_places=0, blank=True, null=True)  
    descricao = models.CharField(db_column='Descricao', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    mes = models.CharField(db_column='Mes', max_length=20, blank=True, null=True)  
    taxames = models.CharField(db_column='TaxaMes', max_length=20, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Juros'

class Multa(models.Model):
        id = models.AutoField(db_column='ID', primary_key=True)  
        valor = models.DecimalField(db_column='Valor', max_digits=38, decimal_places=0, blank=True, null=True)  
        descricao = models.CharField(db_column='Descricao', max_length=150, blank=True, null=True)  
        datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
        dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
        ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
        mes = models.CharField(db_column='Mes', max_length=20, blank=True, null=True)  
        taxames = models.CharField(db_column='TaxaMes', max_length=20, blank=True, null=True)  
        fiscoid = models.ForeignKey(Fisco, on_delete=models.CASCADE, db_column='FiscoID')  

        class Meta:
            managed = False
            db_table = 'Multa'




class Estorno(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    contacontabil = models.CharField(db_column='ContaContabil', max_length=20, blank=True, null=True)  
    esteiracampoid = models.ForeignKey(Esteiracampo, on_delete=models.CASCADE, db_column='EsteiraCampoID')  
    dataestorno = models.DateTimeField(db_column='DataEstorno', blank=True, null=True)  
    usuarioestornoid = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='UsuarioEstornoID', blank=True, null=True)  
    datanf = models.DateTimeField(db_column='DataNF', blank=True, null=True)  
    valor = models.DecimalField(db_column='Valor', max_digits=38, decimal_places=0, blank=True, null=True)  
    tipolancamento = models.CharField(db_column='TipoLancamento', max_length=50, blank=True, null=True)  
    historico = models.CharField(db_column='Historico', max_length=250, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True, blank=True, null=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Estorno'



class Tgcnfam(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    chavenf = models.CharField(db_column='ChaveNF', max_length=50, blank=True, null=True)  
    codigouf = models.CharField(db_column='CodigoUF', max_length=20, blank=True, null=True)  
    naturezaoperacao = models.CharField(db_column='NaturezaOperacao', max_length=50, blank=True, null=True)  
    numeronf = models.CharField(db_column='NumeroNF', max_length=20, blank=True, null=True)  
    dataemissao = models.DateTimeField(db_column='DataEmissao', blank=True, null=True)  
    datafatogerador = models.DateTimeField(db_column='DataFatoGerador', blank=True, null=True)  
    cnpjemitente = models.CharField(db_column='CNPJEmitente', max_length=20, blank=True, null=True)  
    razaosocialemitente = models.CharField(db_column='RazaoSocialEmitente', max_length=100, blank=True, null=True)  
    inscricaoestadualemitente = models.CharField(db_column='InscricaoEstadualEmitente', max_length=20, blank=True, null=True)  
    codigoregimetributario = models.CharField(db_column='CodigoRegimeTributario', max_length=20, blank=True, null=True)  
    cnpjdestinatario = models.CharField(db_column='CNPJDestinatario', max_length=20, blank=True, null=True)  
    razaosocialdestinatario = models.CharField(db_column='RazaoSocialDestinatario', max_length=100, blank=True, null=True)  
    inscricaoestadualdestinatario = models.CharField(db_column='InscricaoEstadualDestinatario', max_length=20, blank=True, null=True)  
    valornf = models.DecimalField(db_column='ValorNF', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoripi = models.DecimalField(db_column='ValorIPI', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoripidevolucao = models.DecimalField(db_column='ValorIPIDevolucao', max_digits=38, decimal_places=0, blank=True, null=True)  
    valorpis = models.DecimalField(db_column='ValorPIS', max_digits=38, decimal_places=0, blank=True, null=True)  
    valorcofins = models.DecimalField(db_column='ValorCOFINS', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoricms = models.DecimalField(db_column='ValorICMS', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisretido = models.DecimalField(db_column='PISRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsretido = models.DecimalField(db_column='COFINSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipiretido = models.DecimalField(db_column='IPIRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipidevolucaoretido = models.DecimalField(db_column='IPIDevolucaoRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    icmsretido = models.DecimalField(db_column='ICMSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisretidoecd = models.DecimalField(db_column='PISRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsretidoecd = models.DecimalField(db_column='COFINSRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipiretidoecd = models.DecimalField(db_column='IPIRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipidevolucaoecd = models.DecimalField(db_column='IPIDevolucaoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    icmsretidoecd = models.DecimalField(db_column='ICMSRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    datapagamentonf = models.DateTimeField(db_column='DataPagamentoNF', blank=True, null=True)  
    statusnf = models.CharField(db_column='StatusNF', max_length=50, blank=True, null=True)  
    datarecebimentonf = models.DateTimeField(db_column='DataRecebimentoNF', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TGCNFAM'


class Tgcnfsp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    prefeiturareferencia = models.CharField(db_column='PrefeituraReferencia', max_length=50, blank=True, null=True)  
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  
    datafatogerador = models.DateTimeField(db_column='DataFatoGerador', blank=True, null=True)  
    cpfcnpjtomador = models.CharField(db_column='CPFCNPJTomador', max_length=20, blank=True, null=True)  
    razaosocialtomador = models.CharField(db_column='RazaoSocialTomador', max_length=150, blank=True, null=True)  
    cidadetomador = models.CharField(db_column='CidadeTomador', max_length=150, blank=True, null=True)  
    uftomador = models.CharField(db_column='UFTomador', max_length=2, blank=True, null=True)  
    valorservico = models.DecimalField(db_column='ValorServico', max_digits=38, decimal_places=0, blank=True, null=True)  
    codigoservico = models.CharField(db_column='CodigoServico', max_length=50, blank=True, null=True)  
    issretido = models.DecimalField(db_column='ISSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issdevido = models.DecimalField(db_column='ISSDevido', max_digits=38, decimal_places=0, blank=True, null=True)  
    isspago = models.DecimalField(db_column='ISSPago', max_digits=38, decimal_places=0, blank=True, null=True)  
    issapagar = models.DecimalField(db_column='ISSAPagar', max_digits=38, decimal_places=0, blank=True, null=True)  
    pispasep = models.DecimalField(db_column='PISPASEP', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofins = models.DecimalField(db_column='COFINS', max_digits=38, decimal_places=0, blank=True, null=True)  
    inss = models.DecimalField(db_column='INSS', max_digits=38, decimal_places=0, blank=True, null=True)  
    ir = models.DecimalField(db_column='IR', max_digits=38, decimal_places=0, blank=True, null=True)  
    csll = models.DecimalField(db_column='CSLL', max_digits=38, decimal_places=0, blank=True, null=True)  
    discriminacaoservicos = models.CharField(db_column='DiscriminacaoServicos', max_length=250, blank=True, null=True)  
    codigocnae = models.CharField(db_column='CodigoCNAE', max_length=50, blank=True, null=True)  
    descricaocnae = models.CharField(db_column='DescricaoCNAE', max_length=150, blank=True, null=True)  
    codigoservicolc = models.CharField(db_column='CodigoServicoLC', max_length=50, blank=True, null=True)  
    descricaoservicolc = models.CharField(db_column='DescricaoServicoLC', max_length=150, blank=True, null=True)  
    pisagriholmes = models.DecimalField(db_column='PISAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsagriholmes = models.DecimalField(db_column='COFINSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfagriholmes = models.DecimalField(db_column='IRRFAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    csllagriholmes = models.DecimalField(db_column='CSLLAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssagriholmes = models.DecimalField(db_column='INSSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisecd = models.DecimalField(db_column='PISECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsecd = models.DecimalField(db_column='COFINSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfecd = models.DecimalField(db_column='IRRFECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    csllecd = models.DecimalField(db_column='CSLLECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssecd = models.DecimalField(db_column='INSSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    datapagamentonf = models.DateTimeField(db_column='DataPagamentoNF', blank=True, null=True)  
    statusnf = models.DateTimeField(db_column='StatusNF', blank=True, null=True)  
    datarecebimentonf = models.DateTimeField(db_column='DataRecebimentoNF', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro')  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TGCNFSP'


class Tgcnfstdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  
    datafatogerador = models.DateTimeField(db_column='DataFatoGerador', blank=True, null=True)  
    cpfcnpjprestador = models.CharField(db_column='CPFCNPJPrestador', max_length=20, blank=True, null=True)  
    razaosocialprestador = models.CharField(db_column='RazaoSocialPrestador', max_length=150, blank=True, null=True)  
    cidadeprestador = models.CharField(db_column='CidadePrestador', max_length=150, blank=True, null=True)  
    ufprestador = models.CharField(db_column='UFPrestador', max_length=2, blank=True, null=True)  
    valorservico = models.DecimalField(db_column='ValorServico', max_digits=38, decimal_places=0, blank=True, null=True)  
    codigoservico = models.CharField(db_column='CodigoServico', max_length=50, blank=True, null=True)  
    issdevido = models.DecimalField(db_column='ISSDevido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issretido = models.DecimalField(db_column='ISSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issrecolhido = models.DecimalField(db_column='ISSRecolhido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issrecolher = models.DecimalField(db_column='ISSRecolher', max_digits=38, decimal_places=0, blank=True, null=True)  
    pispasep = models.DecimalField(db_column='PISPASEP', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofins = models.DecimalField(db_column='COFINS', max_digits=38, decimal_places=0, blank=True, null=True)  
    inss = models.DecimalField(db_column='INSS', max_digits=38, decimal_places=0, blank=True, null=True)  
    ir = models.DecimalField(db_column='IR', max_digits=38, decimal_places=0, blank=True, null=True)  
    csll = models.DecimalField(db_column='CSLL', max_digits=38, decimal_places=0, blank=True, null=True)  
    discriminacaoservicos = models.CharField(db_column='DiscriminacaoServicos', max_length=250, blank=True, null=True)  
    codigocnae = models.CharField(db_column='CodigoCNAE', max_length=50, blank=True, null=True)  
    descricaocnae = models.CharField(db_column='DescricaoCNAE', max_length=150, blank=True, null=True)  
    codigoservicolc = models.CharField(db_column='CodigoServicoLC', max_length=50, blank=True, null=True)  
    descricaoservicolc = models.CharField(db_column='DescricaoServicoLC', max_length=150, blank=True, null=True)  
    pisagriholmes = models.DecimalField(db_column='PISAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsagriholmes = models.DecimalField(db_column='COFINSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfagriholmes = models.CharField(db_column='IRRFAgriholmes', max_length=100, blank=True, null=True)  
    csllagriholmes = models.DecimalField(db_column='CSLLAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssagriholmes = models.DecimalField(db_column='INSSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisecd = models.DecimalField(db_column='PISECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsecd = models.DecimalField(db_column='COFINSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfecd = models.DecimalField(db_column='IRRFECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    csllecd = models.DecimalField(db_column='CSLLECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssecd = models.DecimalField(db_column='INSSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    datapagamentonf = models.DateTimeField(db_column='DataPagamentoNF', blank=True, null=True)  
    statusnf = models.DateTimeField(db_column='StatusNF', blank=True, null=True)  
    datarecebimentonf = models.DateTimeField(db_column='DataRecebimentoNF', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TGCNFSTDM'


class Tgcnfstfm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  
    datafatogerador = models.DateTimeField(db_column='DataFatoGerador', blank=True, null=True)  
    cpfcnpjprestador = models.CharField(db_column='CPFCNPJPrestador', max_length=20, blank=True, null=True)  
    razaosocialprestador = models.CharField(db_column='RazaoSocialPrestador', max_length=150, blank=True, null=True)  
    cidadeprestador = models.CharField(db_column='CidadePrestador', max_length=150, blank=True, null=True)  
    ufprestador = models.CharField(db_column='UFPrestador', max_length=2, blank=True, null=True)  
    valorservico = models.DecimalField(db_column='ValorServico', max_digits=38, decimal_places=0, blank=True, null=True)  
    codigoservico = models.CharField(db_column='CodigoServico', max_length=50, blank=True, null=True)  
    issdevido = models.DecimalField(db_column='ISSDevido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issretido = models.DecimalField(db_column='ISSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issrecolhido = models.DecimalField(db_column='ISSRecolhido', max_digits=38, decimal_places=0, blank=True, null=True)  
    issrecolher = models.DecimalField(db_column='ISSRecolher', max_digits=38, decimal_places=0, blank=True, null=True)  
    pispasep = models.DecimalField(db_column='PISPASEP', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofins = models.DecimalField(db_column='COFINS', max_digits=38, decimal_places=0, blank=True, null=True)  
    inss = models.DecimalField(db_column='INSS', max_digits=38, decimal_places=0, blank=True, null=True)  
    ir = models.DecimalField(db_column='IR', max_digits=38, decimal_places=0, blank=True, null=True)  
    csll = models.DecimalField(db_column='CSLL', max_digits=38, decimal_places=0, blank=True, null=True)  
    discriminacaoservicos = models.CharField(db_column='DiscriminacaoServicos', max_length=250, blank=True, null=True)  
    codigocnae = models.CharField(db_column='CodigoCNAE', max_length=50, blank=True, null=True)  
    descricaocnae = models.CharField(db_column='DescricaoCNAE', max_length=150, blank=True, null=True)  
    codigoservicolc = models.CharField(db_column='CodigoServicoLC', max_length=50, blank=True, null=True)  
    descricaoservicolc = models.CharField(db_column='DescricaoServicoLC', max_length=150, blank=True, null=True)  
    pisagriholmes = models.DecimalField(db_column='PISAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsagriholmes = models.DecimalField(db_column='COFINSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfagriholmes = models.CharField(db_column='IRRFAgriholmes', max_length=100, blank=True, null=True)  
    csllagriholmes = models.DecimalField(db_column='CSLLAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssagriholmes = models.DecimalField(db_column='INSSAgriholmes', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisecd = models.DecimalField(db_column='PISECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsecd = models.DecimalField(db_column='COFINSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    irrfecd = models.DecimalField(db_column='IRRFECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    csllecd = models.DecimalField(db_column='CSLLECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    inssecd = models.DecimalField(db_column='INSSECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    datapagamentonf = models.DateTimeField(db_column='DataPagamentoNF', blank=True, null=True)  
    statusnf = models.DateTimeField(db_column='StatusNF', blank=True, null=True)  
    datarecebimentonf = models.DateTimeField(db_column='DataRecebimentoNF', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TGCNFSTFM'


class Tgcnfvm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    chavenf = models.CharField(db_column='ChaveNF', max_length=50, blank=True, null=True)  
    codigouf = models.CharField(db_column='CodigoUF', max_length=20, blank=True, null=True)  
    naturezaoperacao = models.CharField(db_column='NaturezaOperacao', max_length=50, blank=True, null=True)  
    numeronf = models.CharField(db_column='NumeroNF', max_length=20, blank=True, null=True)  
    dataemissao = models.DateTimeField(db_column='DataEmissao', blank=True, null=True)  
    datafatogerador = models.DateTimeField(db_column='DataFatoGerador', blank=True, null=True)  
    cnpjemitente = models.CharField(db_column='CNPJEmitente', max_length=20, blank=True, null=True)  
    razaosocialemitente = models.CharField(db_column='RazaoSocialEmitente', max_length=100, blank=True, null=True)  
    inscricaoestadualemitente = models.CharField(db_column='InscricaoEstadualEmitente', max_length=20, blank=True, null=True)  
    codigoregimetributario = models.CharField(db_column='CodigoRegimeTributario', max_length=20, blank=True, null=True)  
    cnpjdestinatario = models.CharField(db_column='CNPJDestinatario', max_length=20, blank=True, null=True)  
    razaosocialdestinatario = models.CharField(db_column='RazaoSocialDestinatario', max_length=100, blank=True, null=True)  
    inscricaoestadualdestinatario = models.CharField(db_column='InscricaoEstadualDestinatario', max_length=20, blank=True, null=True)  
    valornf = models.DecimalField(db_column='ValorNF', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoripi = models.DecimalField(db_column='ValorIPI', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoripidevolucao = models.DecimalField(db_column='ValorIPIDevolucao', max_digits=38, decimal_places=0, blank=True, null=True)  
    valorpis = models.DecimalField(db_column='ValorPIS', max_digits=38, decimal_places=0, blank=True, null=True)  
    valorcofins = models.DecimalField(db_column='ValorCOFINS', max_digits=38, decimal_places=0, blank=True, null=True)  
    valoricms = models.DecimalField(db_column='ValorICMS', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisretido = models.DecimalField(db_column='PISRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsretido = models.DecimalField(db_column='COFINSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipiretido = models.DecimalField(db_column='IPIRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipidevolucaoretido = models.DecimalField(db_column='IPIDevolucaoRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    icmsretido = models.DecimalField(db_column='ICMSRetido', max_digits=38, decimal_places=0, blank=True, null=True)  
    pisretidoecd = models.DecimalField(db_column='PISRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    cofinsretidoecd = models.DecimalField(db_column='COFINSRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipiretidoecd = models.DecimalField(db_column='IPIRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    ipidevolucaoecd = models.DecimalField(db_column='IPIDevolucaoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    icmsretidoecd = models.DecimalField(db_column='ICMSRetidoECD', max_digits=38, decimal_places=0, blank=True, null=True)  
    datapagamentonf = models.DateTimeField(db_column='DataPagamentoNF', blank=True, null=True)  
    statusnf = models.CharField(db_column='StatusNF', max_length=50, blank=True, null=True)  
    datarecebimentonf = models.DateTimeField(db_column='DataRecebimentoNF', blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'TGCNFVM'



class TributosBlococampoconfig(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    bloco = models.CharField(db_column='Bloco', max_length=50, blank=True, null=True)  
    campo = models.CharField(db_column='Campo', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Tributos_blococampoconfig'


class TributosControletributos(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    codigocontabil = models.CharField(db_column='CodigoContabil', max_length=50, blank=True, null=True)  
    descricaocodigocontabil = models.CharField(db_column='DescricaoCodigoContabil', max_length=150, blank=True, null=True)  
    mescompetencia = models.IntegerField(db_column='MesCompetencia', blank=True, null=True)  
    anocompetencia = models.IntegerField(db_column='AnoCompetencia', blank=True, null=True)  
    valorprovisaorecolher = models.DecimalField(db_column='ValorProvisaoRecolher', max_digits=38, decimal_places=38, blank=True, null=True)  
    tipolancamentoprevisao = models.CharField(db_column='TipoLancamentoPrevisao', max_length=50, blank=True, null=True)  
    historico = models.CharField(db_column='Historico', max_length=250, blank=True, null=True)  
    vencimento = models.DateField(db_column='Vencimento', blank=True, null=True)  
    datarecolhimento = models.DateField(db_column='DataRecolhimento', blank=True, null=True)  
    valorrecolhimento = models.DecimalField(db_column='ValorRecolhimento', max_digits=38, decimal_places=38, blank=True, null=True)  
    tipolancamento = models.CharField(db_column='TipoLancamento', max_length=50, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  
    mensagemaviso = models.CharField(db_column='MensagemAviso', max_length=250, blank=True, null=True)  
    mensagemrecomendacao = models.CharField(db_column='MensagemRecomendacao', max_length=250, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    esteiraid_id = models.CharField(db_column='EsteiraID_id', max_length=32)  

    class Meta:
        managed = False
        db_table = 'Tributos_controletributos'


class TributosEmpresaregimetributario(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    empresaid_id = models.CharField(db_column='EmpresaID_id', max_length=32)  
    regimetributarioid_id = models.CharField(db_column='RegimeTributarioID_id', max_length=32)  

    class Meta:
        managed = False
        db_table = 'Tributos_empresaregimetributario'


class TributosEsteira(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    empresaid_id = models.CharField(db_column='EmpresaID_id', max_length=32)  
    regimetributarioid_id = models.CharField(db_column='RegimeTributarioID_id', max_length=32)  

    class Meta:
        managed = False
        db_table = 'Tributos_esteira'


class TributosEsteiracampo(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    valor = models.DecimalField(db_column='Valor', max_digits=38, decimal_places=38, blank=True, null=True)  
    blococampoconfig_id = models.CharField(db_column='BlocoCampoConfig_id', max_length=32)  
    esteiraid_id = models.CharField(db_column='EsteiraID_id', max_length=32)  

    class Meta:
        managed = False
        db_table = 'Tributos_esteiracampo'


class TributosRegimetributario(models.Model):

    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    nome = models.CharField(db_column='Nome', max_length=50, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Tributos_regimetributario'


class Obrigacaoacessoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True) 
    versao = models.CharField(db_column='Versao', max_length=20, blank=True, null=True)  
    bloco = models.CharField(db_column='Bloco', max_length=20, blank=True, null=True)  
    campo = models.CharField(db_column='Campo', max_length=20, blank=True, null=True)  
    datacadastro = models.DateTimeField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateTimeField(db_column='DataAlteracao', auto_now=True,blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    blococampoconfigid = models.ForeignKey(Blococampoconfig, on_delete=models.CASCADE, db_column='BlocoCampoConfigID')  
    escopo = models.CharField(db_column='Escopo', max_length=50)  
    posicaotxt = models.CharField(db_column='PosicaoTXT', max_length=20, blank=True, null=True)  
    tamanho = models.CharField(db_column='Tamanho', max_length=20, blank=True, null=True)  
    paginamanual = models.CharField(db_column='PaginaManual', max_length=100, blank=True, null=True)  
    observacao = models.CharField(db_column='Observacao', max_length=250, blank=True, null=True)  
    registro = models.CharField(db_column='Registro', max_length=150, blank=True, null=True)  
    ordemclassificacao = models.CharField(db_column='OrdemClassificacao', max_length=20, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'ObrigacaoAcessoria'



class ObrigacaoacessoriaObrigacaoacessoria(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  
    versao = models.CharField(db_column='Versao', max_length=20, blank=True, null=True)  
    bloco = models.CharField(db_column='Bloco', max_length=20, blank=True, null=True)  
    campo = models.CharField(db_column='Campo', max_length=20, blank=True, null=True)  
    datacadastro = models.DateField(db_column='DataCadastro', auto_now_add=True)  
    dataalteracao = models.DateField(db_column='DataAlteracao', auto_now=True, blank=True, null=True)  
    ativo = models.BooleanField(db_column='Ativo', default=True, blank=True, null=True)  
    escopo = models.CharField(db_column='Escopo', max_length=50)  
    posicaotxt = models.CharField(db_column='PosicaoTXT', max_length=20, blank=True, null=True)  
    tamanho = models.CharField(db_column='Tamanho', max_length=20, blank=True, null=True)  
    paginamanual = models.CharField(db_column='PaginaManual', max_length=100, blank=True, null=True)  
    observacao = models.CharField(db_column='Observacao', max_length=250, blank=True, null=True)  
    registro = models.CharField(db_column='Registro', max_length=150, blank=True, null=True)  
    ordemclassificacao = models.CharField(db_column='OrdemClassificacao', max_length=20, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'ObrigacaoAcessoria_obrigacaoacessoria'




class Esteirajuros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    jurosid = models.ForeignKey(Juros, on_delete=models.CASCADE, db_column='JurosID')  

    class Meta:
        managed = False
        db_table = 'EsteiraJuros'



class Esteiramulta(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    multaid = models.ForeignKey(Multa, on_delete=models.CASCADE, db_column='MultaID')  
    obrigacaoacessoriaid = models.ForeignKey(Obrigacaoacessoria, on_delete=models.CASCADE, db_column='ObrigacaoAcessoriaID', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'EsteiraMulta'



class Esteiraobrigacaoacessoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  
    esteiraid = models.ForeignKey(Esteira, on_delete=models.CASCADE, db_column='EsteiraID')  
    obrigacaoacessoriaid = models.ForeignKey(Obrigacaoacessoria, on_delete=models.CASCADE, db_column='ObrigacaoAcessoriaID')  

    class Meta:
        managed = False
        db_table = 'EsteiraObrigacaoAcessoria'