from django.contrib import admin
from .models import Cliente, ClienteEmpresa

# Register your models here.

admin.site.register(Cliente)
admin.site.register(ClienteEmpresa)