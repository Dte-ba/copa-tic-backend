from django.contrib import admin
from copatic.models.escuela import Escuela

class EscuelaAdmin(admin.ModelAdmin):
    model = Escuela
    list_display = ('id', 'nombre', 'localidad', 'latitud', 'longitud')
    search_fields = ('nombre', 'localidad')
