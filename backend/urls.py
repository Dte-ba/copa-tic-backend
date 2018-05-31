from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from copatic.views.escuela import EscuelaViewSet
from copatic.views.equipo import EquipoViewSet
from copatic.views.insignia import InsigniaViewSet
from copatic.views.actividad import ActividadViewSet
from copatic.views.home import home

router = routers.DefaultRouter(trailing_slash=False)
router.register('escuelas', EscuelaViewSet)
router.register('equipos', EquipoViewSet)
router.register('insignias', InsigniaViewSet)
router.register('actividades', ActividadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home, name='home')
]
