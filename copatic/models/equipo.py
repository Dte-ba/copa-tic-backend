from django.db import models
from copatic.models.actividad import Actividad

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

    def insignias_ganadas(self):
        actividades_terminadas = []
        insignias_ganadas = []

        if self.a1estado == True:
            actividad = Actividad.objects.get(id=1)
            insignias = actividad.insignias
            actividades_terminadas.append("a1")
        if self.a2estado == True:
            actividades_terminadas.append("a2")
        if self.a3estado == True:
            actividades_terminadas.append("a3")
        if self.a4estado == True:
            actividades_terminadas.append("a4")
        if self.a5estado == True:
            actividades_terminadas.append("a5")
        if self.a6estado == True:
            actividades_terminadas.append("a6")
        if self.a7estado == True:
            actividades_terminadas.append("a7")
        if self.a8estado == True:
            actividades_terminadas.append("a8")
        if self.a9estado == True:
            actividades_terminadas.append("a9")
        if self.a10estado == True:
            actividades_terminadas.append("a10")
        if self.a11estado == True:
            actividades_terminadas.append("a11")
        if self.a12estado == True:
            actividades_terminadas.append("a12")
        if self.a13estado == True:
            actividades_terminadas.append("a13")
        if self.a14estado == True:
            actividades_terminadas.append("a14")
        if self.a15estado == True:
            actividades_terminadas.append("a15")
        if self.a16estado == True:
            actividades_terminadas.append("a16")

        return actividades_terminadas
