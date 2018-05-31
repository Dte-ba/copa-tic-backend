from django.db import models

class Insignia(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'insignias'
        verbose_name_plural = "insignias"

    class JSONAPIMeta:
        resource_name = 'insignias'
