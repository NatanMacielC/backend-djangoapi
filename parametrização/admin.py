from django.contrib import admin
from django.db import models
from parametrização.models import Documento, Cnae, Codigoprefeitura, Deparacnaecodigoprefeitura, Deparacnaeleicomplementar, Deparaleicomplementarretencao, Evento, Eventogrupo, Geracaocredito, Grupoevento, Leicomplementar, Parametrizacao, Parametrizacaoregra, Periodicidade, Regra, Regradocumento, Retencaofonte, Tipoarquivo   

# Register your models here.
admin.site.register(Documento)
admin.site.register(Cnae)
admin.site.register(Codigoprefeitura)
admin.site.register(Deparacnaecodigoprefeitura)
admin.site.register(Deparacnaeleicomplementar)
admin.site.register(Deparaleicomplementarretencao)
admin.site.register(Evento)
admin.site.register(Eventogrupo)
admin.site.register(Geracaocredito)
admin.site.register(Grupoevento)
admin.site.register(Leicomplementar)
admin.site.register(Parametrizacao)
admin.site.register(Parametrizacaoregra)
admin.site.register(Periodicidade)
admin.site.register(Regra)
admin.site.register(Regradocumento)
admin.site.register(Retencaofonte)
admin.site.register(Tipoarquivo)

