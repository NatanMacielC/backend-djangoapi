from django.contrib import admin
from .models import Cliente, ClienteCliente, ClienteClienteempresa, Grupo

# Register your models here.

admin.site.register(Cliente)
admin.site.register(ClienteCliente)
admin.site.register(Grupo)
admin.site.register(ClienteClienteempresa)