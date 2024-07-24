from django.contrib import admin
from .models import Cliente, Salida, Localidd, Municip, Produc, Categ, Entradas, Proveedor


# Register your models here.
admin.site.register(Entradas)
admin.site.register(Proveedor)
admin.site.register(Categ)
admin.site.register(Produc)
admin.site.register(Municip)
admin.site.register(Localidd)
admin.site.register(Cliente)
admin.site.register(Salida)
