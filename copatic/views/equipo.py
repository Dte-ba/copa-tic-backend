from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from copatic.models.equipo import Equipo
from copatic.serializers.equipo import EquipoSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by("-eid")
    resource_name = 'equipos'

    serializer_class = EquipoSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'escuela__nombre']
    filter_fields = ['nombre']
