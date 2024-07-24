from django.db import models
   
class Reporte(models.Model):
    code = models.CharField(max_length=50, verbose_name="Codigo")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    amount = models.PositiveIntegerField(verbose_name="Cantidad")
    price = models.PositiveIntegerField(verbose_name="Precio")
    customer = models.CharField(max_length=200, verbose_name="Cliente")
    location = models.CharField(max_length=150, verbose_name="Localidad")
    image = models.ImageField(verbose_name="Capturar", upload_to="projects")
    #link = models.URLField(verbose_name="Direccion Web", null=True, blank=True)
    # upload_to="projects"
    created = models.DateField(
        auto_now_add=True, verbose_name="Fecha de registro")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de modificacion")

    class Meta:
        verbose_name = "reporte"
        verbose_name_plural = "reportes"
        ordering = ["-created"]
        
    def __str__(self):
        return self.name