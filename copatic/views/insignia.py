from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from copatic.models.insignia import Insignia
from copatic.serializers.insignia import InsigniaSerializer

class InsigniaViewSet(viewsets.ModelViewSet):
    queryset = Insignia.objects.all()
    resource_name = 'insignias'

    serializer_class = InsigniaSerializer
    search_fields = ['nombre']
    filter_fields = ['nombre']
