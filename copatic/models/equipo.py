from django.db import models

class Equipo(models.Model):
    escuela = models.ForeignKey('Escuela', on_delete=models.CASCADE, related_name='equipos', default=None, blank=True, null=True)
    eid = models.CharField(max_length=4, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    a1estado = models.BooleanField(default=False)
    a1link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a2estado = models.BooleanField(default=False)
    a2link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a3estado = models.BooleanField(default=False)
    a3link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a4estado = models.BooleanField(default=False)
    a4link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a5estado = models.BooleanField(default=False)
    a5link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a6estado = models.BooleanField(default=False)
    a6link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a7estado = models.BooleanField(default=False)
    a7link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a8estado = models.BooleanField(default=False)
    a8link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a9estado = models.BooleanField(default=False)
    a9link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a10estado = models.BooleanField(default=False)
    a10link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a11estado = models.BooleanField(default=False)
    a11link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a12estado = models.BooleanField(default=False)
    a12link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a13estado = models.BooleanField(default=False)
    a13link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a14estado = models.BooleanField(default=False)
    a14link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a15estado = models.BooleanField(default=False)
    a15link = models.CharField(max_length=100,default=None, blank=True, null=True)
    a16estado = models.BooleanField(default=False)
    a16link = models.CharField(max_length=100,default=None, blank=True, null=True)

    class Meta:
        db_table = 'equipos'
        verbose_name_plural = "equipos"

    class JSONAPIMeta:
        resource_name = 'equipos'
