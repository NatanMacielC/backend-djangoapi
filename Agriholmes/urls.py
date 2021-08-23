"""Agriholmes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# django apps
from django import urls
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include 
# views
from empresa.api import viewsets as empresaviewsets
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from calendario import viewsets as calendarviewsets
from parametrização import views as parameterviewsets
from fisco import views as fiscoviewsets
from cliente import views as clienteviewsets
from planocontas import views as planocontasviewsets
from tributos import views as tributosviewsets
# modules
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

route = routers.DefaultRouter()


# Empresa
route.register(r'Empresa', empresaviewsets.EmpresaViewSet, basename="Empresa")
route.register(r'Fornecedor', empresaviewsets.FornecedorViewSet, basename="Fornecedor")
route.register(r'EmpresaPlanoContas', empresaviewsets.EmpresaplanocontasViewSet, basename="Empresaplanocontas")
route.register(r'GrupoEmpresa', empresaviewsets.GrupoempresaViewSet, basename="Grupoempresa")

# Calendario
route.register(r'Calendario', calendarviewsets.CalendarioViewSet, basename="Calendario")
route.register(r'CalendarioFeriado', calendarviewsets.CalendarioferiadoViewSet, basename="Feriado")

# Cliente
route.register(r'Cliente', clienteviewsets.ClienteViewSet, basename="Cliente")
route.register(r'ClienteCliente', clienteviewsets.ClienteclienteViewSet, basename="ClienteCliente")
route.register(r'Grupo', clienteviewsets.GrupoViewSet, basename="Grupo")

# Parametrização
route.register(r'Evento', parameterviewsets.EventoViewSet, basename="Evento")
route.register(r'Regras', parameterviewsets.RegrasViewSet, basename="Regras")
route.register(r'Cnae', parameterviewsets.CnaeViewSet, basename="Cnae")
route.register(r'Geracaocredito', parameterviewsets.GeracaocreditoViewSet, basename="Geracaocredito")
route.register(r'Retencaofonte', parameterviewsets.RetencaofonteViewSet, basename="Retencaofonte")
route.register(r'Periodicidade', parameterviewsets.PeriodicidadeViewSet, basename="Periodicidade")
route.register(r'Grupoevento', parameterviewsets.GrupoeventoViewSet, basename="Grupoevento")
route.register(r'Eventogrupo', parameterviewsets.EventogrupoViewSet, basename="Eventogrupo")
route.register(r'Parametrizacao', parameterviewsets.ParametrizacaoViewSet, basename="Parametrizacao")
route.register(r'Parametrizacaoregra', parameterviewsets.ParametrizacaoregraViewSet, basename="Parametrizacaoregra")
route.register(r'Codigoprefeitura', parameterviewsets.CodigoprefeituraViewSet, basename="Codigoprefeitura")
route.register(r'Leicomplementar', parameterviewsets.LeicomplementarViewSet, basename="Leicomplementar")
route.register(r'Documento', parameterviewsets.DocumentoViewSet, basename="Documento")
route.register(r'Regradocumento', parameterviewsets.RegradocumentoViewSet, basename="Regradocumento")
route.register(r'Tipoarquivo', parameterviewsets.TipoarquivoViewSet, basename="Tipoarquivo")
route.register(r'Deparacnaecodigoprefeitura', parameterviewsets.DeparacnaecodigoprefeituraViewSet, basename="Deparacnaecodigoprefeitura")
route.register(r'Deparacnaeleicomplementar', parameterviewsets.DeparacnaeleicomplementarViewSet, basename="Deparacnaeleicomplementar")
route.register(r'Deparaleicomplementarretencao', parameterviewsets.DeparaleicomplementarretencaoViewSet, basename="Deparaleicomplementarretencao")

# Fisco
route.register(r'Fisco', fiscoviewsets.FiscoViewSet, basename="Fisco")
route.register(r'FiscoCalendario', fiscoviewsets.FiscocalendarioViewSet, basename="FiscoCalendario")

# Plano Contas
route.register(r'PlanocontasPlanocontasreferencial', planocontasviewsets.PlanocontasPlanocontasreferencialViewSet, basename="PlanocontasPlanocontasreferencial")
route.register(r'Planocontasreferencial', planocontasviewsets.PlanocontasreferencialViewSet, basename="Planocontasreferencial")

# Tributos
route.register(r'RegimeTributario', tributosviewsets.RegimeTributarioViewSet, basename="RegimeTributario")
route.register(r'Empresaregimetributario', tributosviewsets.EmpresaregimetributarioViewSet, basename="Empresaregimetributario")
route.register(r'Controletributos', tributosviewsets.ControletributosViewSet, basename="Controletributos")
route.register(r'Blococampoconfig', tributosviewsets.BlococampoconfigViewSet, basename="Blococampoconfig")
route.register(r'Juros', tributosviewsets.JurosViewSet, basename="Juros")
route.register(r'Multa', tributosviewsets.MultaViewSet, basename="Multa")
route.register(r'Estorno', tributosviewsets.EstornoViewSet, basename="Estorno")
route.register(r'Tgcnfam', tributosviewsets.TgcnfamViewSet, basename="Tgcnfam")
route.register(r'Tgcnfsp', tributosviewsets.TgcnfspViewSet, basename="Tgcnfsp")
route.register(r'Tgcnfstdm', tributosviewsets.TgcnfstdmViewSet, basename="Tgcnfstdm")
route.register(r'Tgcnfstfm', tributosviewsets.TgcnfstfmViewSet, basename="Tgcnfstfm")
route.register(r'Tgcnfvm', tributosviewsets.TgcnfvmViewSet, basename="Tgcnfvm")
route.register(r'TributosBlococampoconfig', tributosviewsets.TributosBlococampoconfigViewSet, basename="TributosBlococampoconfig")
route.register(r'TributosControletributos', tributosviewsets.TributosControletributosViewSet, basename="TributosControletributos")
route.register(r'TributosEmpresaregimetributario', tributosviewsets.TributosEmpresaregimetributarioViewSet, basename="TributosEmpresaregimetributario")
route.register(r'TributosEsteira', tributosviewsets.TributosEsteiraViewSet, basename="TributosEsteira")
route.register(r'TributosEsteiracampo', tributosviewsets.TributosEsteiracampoViewSet, basename="TributosEsteiracampo")
route.register(r'TributosRegimetributario', tributosviewsets.TributosRegimetributarioViewSet, basename="TributosRegimetributario")
route.register(r'Esteira', tributosviewsets.EsteiraViewSet, basename="Esteira")
route.register(r'Esteiracampo', tributosviewsets.EsteiracampoViewSet, basename="Esteiracampo")
route.register(r'Obrigacaoacessoria', tributosviewsets.ObrigacaoacessoriaViewSet, basename="Obrigacaoacessoria")
route.register(r'Esteirajuros', tributosviewsets.EsteirajurosViewSet, basename="Esteirajuros")
route.register(r'Esteiramulta', tributosviewsets.EsteiramultaViewSet, basename="Esteiramulta")
route.register(r'Esteiraobrigacaoacessoria', tributosviewsets.EsteiraobrigacaoacessoriaViewSet, basename="Esteiraobrigacaoacessoria")
route.register(r'ObrigacaoacessoriaObrigacaoacessoria', tributosviewsets.ObrigacaoacessoriaObrigacaoacessoriaViewSet, basename="ObrigacaoacessoriaObrigacaoacessoria")


urlpatterns = [
    # django admin
    path('admin/', admin.site.urls),
    # home
    path('', include(route.urls)),
    # authentication
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path(r'^', include('calendario.urls')),
    path(r'^', include('parametrização.urls')),
    path(r'^', include('fisco.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]