from django.contrib import admin
from .models import Catalago, Sucursales, Contactos, Discounts


# Register your models here.
class SucursalesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

#Para funcinar
admin.site.register(Sucursales, SucursalesAdmin)

# Register your models here.
class ContactosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Contactos, ContactosAdmin)

# Register your models here.
class DescuentosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Discounts, DescuentosAdmin)

class CatalagoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Catalago, CatalagoAdmin)