from django.contrib import admin
from copatic.models.fase import Fase

class FaseAdmin(admin.ModelAdmin):
    model = Fase
    list_display = ('id', 'nombre', 'estado')
    search_fields = ['nombre']
