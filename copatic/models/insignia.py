from django.db import models

class Insignia(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        db_table = 'insignias'
        verbose_name_plural = "insignias"

    class JSONAPIMeta:
        resource_name = 'insignias'
