from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from copatic.models.fase import Fase
from copatic.serializers.fase import FaseSerializer

class FaseViewSet(viewsets.ModelViewSet):
    queryset = Fase.objects.all()
    resource_name = 'fases'

    serializer_class = FaseSerializer
    search_fields = ['nombre']
    filter_fields = ['nombre']
