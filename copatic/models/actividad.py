from django.db import models

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    fase = models.IntegerField(default=None)
    puntos = models.IntegerField(default=None)

    class Meta:
        db_table = 'actividades'
        verbose_name_plural = "actividades"

    class JSONAPIMeta:
        resource_name = 'actividades'
