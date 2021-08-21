from django.contrib import admin

# Register your models here.

from .models import Empresa, Empresaplanocontas, Fornecedor, Grupoempresa, PlanocontasEmpresaplanocontas

admin.site.register(Empresa)
admin.site.register(Empresaplanocontas)
admin.site.register(Fornecedor)
admin.site.register(Grupoempresa)
admin.site.register(PlanocontasEmpresaplanocontas)
