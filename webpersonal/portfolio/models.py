# pylint: disable=trailing-whitespace
from django.db import models

# Create your models here.

class Sucursales(models.Model):
    code = models.CharField(max_length=200, verbose_name="Numero de Sucursal")
    name = models.CharField(max_length=200, verbose_name="Localidad")
    municipio = models.CharField(max_length=200, verbose_name="Municipio")
    description = models.TextField(verbose_name="Descripción")
    Horario = models.CharField(max_length=200, verbose_name="Horario de atención")
    Dias = models.CharField(max_length=200, verbose_name="Dias de atención") 
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
    Puesto = models.CharField(max_length=200, verbose_name="Puesto")
    email = models.CharField(max_length=200, verbose_name="Email")
    phone = models.CharField(max_length=200, verbose_name="Telefono")
    image = models.ImageField(verbose_name="Imagen", upload_to="Contacts")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contactos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name

class Descuentos(models.Model):
    code = models.CharField(max_length=200, verbose_name="Codigo De Producto")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    preci = models.PositiveIntegerField(verbose_name="Precio")
    descuento = models.PositiveIntegerField(verbose_name="Descuento")
    Cantidad = models.PositiveIntegerField(verbose_name="Cantidad")    
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

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.title
    
