from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from copatic.models.escuela import Escuela
from copatic.serializers.escuela import EscuelaSerializer

class EscuelaViewSet(viewsets.ModelViewSet):
    queryset = Escuela.objects.all()
    resource_name = 'escuelas'

    serializer_class = EscuelaSerializer
    # filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'localidad']
    filter_fields = ['nombre', 'localidad']
