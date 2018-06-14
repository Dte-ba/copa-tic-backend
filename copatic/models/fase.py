from django.db import models

class Fase(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'etapas'
        verbose_name_plural = "etapas"

    class JSONAPIMeta:
        resource_name = 'etapas'
