from django.contrib import admin
from .models import ControleTributos, EmpresaRegimeTributario, Esteira, RegimeTributario, BlocoCampoConfig, EsteiraCampo

# Register your models here.

admin.site.register(EmpresaRegimeTributario)
admin.site.register(ControleTributos)
admin.site.register(Esteira)
admin.site.register(RegimeTributario)
admin.site.register(BlocoCampoConfig)
admin.site.register(EsteiraCampo)


