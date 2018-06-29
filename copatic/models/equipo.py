from django.db import models
from copatic.models.actividad import Actividad
from copatic.models.insignia import Insignia

class Equipo(models.Model):
    escuela = models.ForeignKey('Escuela', on_delete=models.CASCADE, related_name='equipos', default=None, blank=True, null=True)
    eid = models.CharField(max_length=4, default=None, blank=True, null=True)
    nombre = models.CharField(max_length=250)
    dt = models.CharField(max_length=100)
    puntos = models.IntegerField(default=0)

    a1estado = models.BooleanField(default=False)
    a1link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a2estado = models.BooleanField(default=False)
    a2link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a3estado = models.BooleanField(default=False)
    a3link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a4estado = models.BooleanField(default=False)
    a4link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a5estado = models.BooleanField(default=False)
    a5link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a6estado = models.BooleanField(default=False)
    a6link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a7estado = models.BooleanField(default=False)
    a7link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a8estado = models.BooleanField(default=False)
    a8link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a9estado = models.BooleanField(default=False)
    a9link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a10estado = models.BooleanField(default=False)
    a10link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a11estado = models.BooleanField(default=False)
    a11link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a12estado = models.BooleanField(default=False)
    a12link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a13estado = models.BooleanField(default=False)
    a13link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a14estado = models.BooleanField(default=False)
    a14link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a15estado = models.BooleanField(default=False)
    a15link = models.CharField(max_length=250,default=None, blank=True, null=True)
    a16estado = models.BooleanField(default=False)
    a16link = models.CharField(max_length=250,default=None, blank=True, null=True)

    class Meta:
        ordering = ['eid']
        db_table = 'equipos'
        verbose_name_plural = "equipos"

    class JSONAPIMeta:
        resource_name = 'equipos'

    def tieneInsignia(self, insignia):
        actividades_terminadas = []
        insignias_ganadas = []

        if self.a1estado == True:
            actividad = Actividad.objects.get(id=1)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a1")
        if self.a2estado == True:
            actividad = Actividad.objects.get(id=2)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a2")
        if self.a3estado == True:
            actividad = Actividad.objects.get(id=3)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a3")
        if self.a4estado == True:
            actividad = Actividad.objects.get(id=4)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a4")
        if self.a5estado == True:
            actividad = Actividad.objects.get(id=5)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a5")
        if self.a6estado == True:
            actividad = Actividad.objects.get(id=6)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a6")
        if self.a7estado == True:
            actividad = Actividad.objects.get(id=7)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a7")
        if self.a8estado == True:
            actividad = Actividad.objects.get(id=8)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a8")
        if self.a9estado == True:
            actividad = Actividad.objects.get(id=9)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a9")
        if self.a10estado == True:
            actividad = Actividad.objects.get(id=10)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a10")
        if self.a11estado == True:
            actividad = Actividad.objects.get(id=11)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a11")
        if self.a12estado == True:
            actividad = Actividad.objects.get(id=12)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a12")
        if self.a13estado == True:
            actividad = Actividad.objects.get(id=13)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a13")
        if self.a14estado == True:
            actividad = Actividad.objects.get(id=14)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a14")
        if self.a15estado == True:
            actividad = Actividad.objects.get(id=15)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a15")
        if self.a16estado == True:
            actividad = Actividad.objects.get(id=16)
            for i in actividad.insignias.all():
                insignias_ganadas.append(i.slug)
            actividades_terminadas.append("a16")

        return insignia.slug in insignias_ganadas

    def insignias_ganadas(self):

        todas_las_insignias = Insignia.objects.all()
        retorno = []

        for insignia in todas_las_insignias:
            retorno.append({"nombre": insignia.slug, "tiene": self.tieneInsignia(insignia)})


        return retorno
