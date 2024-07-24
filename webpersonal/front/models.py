from django.db import models

from stored.models import Categ, Localidd, Municip, Produc

# Create your models here.

class Discounts(models.Model):
    Codigo = models.ForeignKey(
        Produc, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    discount = models.PositiveIntegerField(verbose_name="Descuento")
    price = models.PositiveIntegerField(verbose_name="Precio")
    startt = models.PositiveIntegerField(verbose_name="Dia de inicio")
    startMonth = models.PositiveIntegerField(verbose_name="Mes de inicio")
    ending = models.PositiveIntegerField(verbose_name="Dia de finalizacion")
    monthOfCompletion = models.PositiveIntegerField(verbose_name="Mes de finalizacion")
    year = models.PositiveIntegerField(verbose_name="Año")
    amount = models.PositiveIntegerField(verbose_name="Cantidad")
    image = models.ImageField(verbose_name="Imagen", upload_to="Descuents")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "descuento"
        verbose_name_plural = "descuentos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name
    
class Sucursales(models.Model):
    code = models.CharField(max_length=200, verbose_name="Numero de Tienda")
    localidad = models.ForeignKey(
        Localidd, null=True, blank=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        Municip, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descripción")
    schedule = models.CharField(max_length=200, verbose_name="Horario de atención")
    days = models.CharField(max_length=200, verbose_name="Dias de atención") 
    image = models.ImageField(verbose_name="Imagen", upload_to="Sucursals")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "sucursal"
        verbose_name_plural = "sucursales"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name

class Contactos(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombres")
    last = models.CharField(max_length=200, verbose_name="Apellidos")
    position = models.CharField(max_length=200, verbose_name="Puesto")
    email = models.CharField(max_length=200, verbose_name="Email")
    phone = models.CharField(max_length=200, verbose_name="Telefono")
    image = models.ImageField(verbose_name="Imagen", upload_to="Contacts")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "contacto"
        verbose_name_plural = "contactos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name


class Catalago(models.Model):
    Codigo = models.ForeignKey(
        Produc, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    categoria = models.ForeignKey(
        Categ, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Descripción")
    price = models.PositiveIntegerField(verbose_name="Precio")
    amount = models.PositiveIntegerField(verbose_name="Cantidad")
    extent = models.CharField(max_length=200, verbose_name="Tipo de medidas Kg. o L. ")
    image = models.ImageField(verbose_name="Imagen", upload_to="Catalags")
    #link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    # upload_to="projects"
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "catalago"
        verbose_name_plural = "catalagos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name