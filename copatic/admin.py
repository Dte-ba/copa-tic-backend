from django.contrib import admin
from copatic.admin_classes.escuela import Escuela, EscuelaAdmin
from copatic.admin_classes.equipo import Equipo, EquipoAdmin

admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Equipo, EquipoAdmin)
