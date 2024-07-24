from django.db import models
from .choices import sexos, estado

# Create your models here.


class Categ(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Produc(models.Model):
    code = models.CharField(max_length=200, verbose_name="codigo")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    price = models.PositiveIntegerField(verbose_name="Precio")
    expiration = models.CharField(max_length=40, verbose_name="Caducidad")
    categoria = models.ForeignKey(
        Categ, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Capturar", upload_to="Products")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-created"]
        
    def __str__(self):
        return self.code


class Municip(models.Model):
    code = models.CharField(max_length=50, verbose_name="Codigo Postal")
    name = models.CharField(max_length=80, verbose_name="Municipio")
    estado = models.CharField(max_length=50, choices=estado, default='1')
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")
    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Localidd(models.Model):
    code = models.CharField(max_length=50, verbose_name="Codigo Postal")
    name = models.CharField(max_length=80, verbose_name="Localidad")
    municipalit = models.CharField(max_length=80, verbose_name="Municipio")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")
    class Meta:
        verbose_name = "Localidad"
        verbose_name_plural = "Localidades"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Proveedor(models.Model):
    code = models.CharField(max_length=50, verbose_name="Identificacion")
    name = models.CharField(max_length=80, verbose_name="Nombres")
    last = models.CharField(max_length=80, verbose_name="Apellidos")
    description = models.TextField(verbose_name="Descripción")
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    company = models.CharField(max_length=150, verbose_name="Empresa")
    phone = models.CharField(max_length=100, verbose_name="Telefono")
    mail = models.CharField(max_length=100, verbose_name="Correo Electronico")
    image = models.ImageField(verbose_name="Capturar", upload_to="proveeds")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")
    
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Provedores"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Cliente(models.Model):
    code = models.CharField(max_length=50, verbose_name="Identificacion")
    name = models.CharField(max_length=80, verbose_name="Nombres")
    last = models.CharField(max_length=80, verbose_name="Apellidos")
    description = models.TextField(verbose_name="Descripción")
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    localidad = models.ForeignKey(
        Localidd, null=True, blank=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        Municip, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, verbose_name="Telefono")
    image = models.ImageField(verbose_name="Capturar", upload_to="clients")
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")
    

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    

class Entradas(models.Model):
    codigo = models.ForeignKey(
        Produc, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    amount = models.PositiveIntegerField(verbose_name="Cantidad")
    price = models.PositiveIntegerField(verbose_name="Precio")
    expiration = models.CharField(max_length=40, verbose_name="Caducidad")
    categoria = models.ForeignKey(
        Categ, null=True, blank=True, on_delete=models.CASCADE)
    porveedor = models.ForeignKey(
        Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Capturar",
                              upload_to="salidaProducts")
    # link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    # upload_to="projects"
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Entrada De Producto"
        verbose_name_plural = "Entradas De Productos"
        ordering = ["-created"]

    def __str__(self):
        return self.name


class Salida(models.Model):
    codigo = models.ForeignKey(
        Produc, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    amount = models.PositiveIntegerField(verbose_name="Cantidad")
    price = models.PositiveIntegerField(verbose_name="Precio")
    expiration = models.CharField(max_length=40, verbose_name="Caducidad")
    categoria = models.ForeignKey(
        Categ, null=True, blank=True, on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, null=True, blank=True, on_delete=models.CASCADE)
    localidad = models.ForeignKey(
        Localidd, null=True, blank=True, on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        Municip, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Capturar",
                              upload_to="salidaProducts")
    # link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    # upload_to="projects"
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "Salida De Producto"
        verbose_name_plural = "Salidas De Productos"
        ordering = ["-created"]

    def __str__(self):
        return self.name
