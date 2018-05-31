from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from copatic.models.actividad import Actividad
from copatic.serializers.actividad import ActividadSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    resource_name = 'actividades'

    serializer_class = ActividadSerializer
    search_fields = ['nombre']
    filter_fields = ['nombre']
