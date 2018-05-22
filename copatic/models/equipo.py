from django.db import models

class Equipo(models.Model):
    escuela = models.ForeignKey('Escuela', on_delete=models.CASCADE, related_name='equipos', default=None, blank=True, null=True)
    eid = models.CharField(max_length=4, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    class Meta:
        db_table = 'equipos'
        verbose_name_plural = "equipos"

    class JSONAPIMeta:
        resource_name = 'equipos'
