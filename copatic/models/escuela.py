from django.db import models

class Escuela(models.Model):
    cue = models.CharField(max_length=8, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    latitud = models.CharField(max_length=64, default=None, blank=True, null=True)
    longitud = models.CharField(max_length=64, default=None, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'escuelas'
        verbose_name_plural = "escuelas"

    class JSONAPIMeta:
        resource_name = 'escuelas'
