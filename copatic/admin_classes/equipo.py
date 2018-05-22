from django.contrib import admin
from copatic.models.equipo import Equipo

class EquipoAdmin(admin.ModelAdmin):
    model = Equipo
    list_display = ('id', 'eid', 'nombre', 'dt', 'puntos')
    search_fields = ('nombre', 'dt')
