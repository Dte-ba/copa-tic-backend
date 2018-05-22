from rest_framework import serializers
from copatic.models.equipo import Equipo

class EquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = ('id', 'eid', 'escuela', 'nombre', 'dt', 'puntos')
