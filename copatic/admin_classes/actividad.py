from django.contrib import admin
from copatic.models.actividad import Actividad

class ActividadAdmin(admin.ModelAdmin):
    model = Actividad
    list_display = ('id', 'titulo', 'fase', 'puntos', 'descripcion')
    search_fields = ['titulo']
