from django.contrib import admin
from .models import Project, Sucursales, Contactos, Descuentos


# Register your models here.
class SucursalesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Sucursales, SucursalesAdmin)

# Register your models here.
class ContactosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Contactos, ContactosAdmin)

# Register your models here.
class DescuentosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Descuentos, DescuentosAdmin)
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')


admin.site.register(Project, ProjectAdmin)