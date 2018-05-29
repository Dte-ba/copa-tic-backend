from django.db import models

class Actividad(models.Model):
    titulo = models.CharField(max_length=100)
    fase = models.IntegerField(default=None)
    puntos = models.IntegerField(default=None)
    descripcion = models.TextField(default=None)

    insignias = models.ManyToManyField("Insignia", related_name="actividades", default=None, blank=True)

    class Meta:
        db_table = 'actividades'
        verbose_name_plural = "actividades"

    class JSONAPIMeta:
        resource_name = 'actividades'
