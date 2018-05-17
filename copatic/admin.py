from django.contrib import admin
from copatic import models


class CustomModelAdmin(admin.ModelAdmin):

    class Media:
         js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            )

class EscuelaAdmin(CustomModelAdmin):
    model = models.Escuela
    list_display = ('id', 'nombre', 'localidad')
    search_fields = ('nombre', 'localidad')


admin.site.register(models.Escuela, EscuelaAdmin)
