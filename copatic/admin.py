from django.contrib import admin
from copatic.admin_classes.escuela import Escuela, EscuelaAdmin
from copatic.admin_classes.equipo import Equipo, EquipoAdmin
from copatic.admin_classes.actividad import Actividad, ActividadAdmin
from copatic.admin_classes.insignia import Insignia, InsigniaAdmin

admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Insignia, InsigniaAdmin)
