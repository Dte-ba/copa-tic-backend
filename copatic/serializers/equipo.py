from rest_framework import serializers
from copatic.models.equipo import Equipo

class EquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = ('id', 'eid', 'escuela', 'nombre', 'dt', 'puntos', 'a1estado', 'a1link', 'a2estado', 'a2link', 'a3estado', 'a3link', 'a4estado', 'a4link', 'a5estado', 'a5link', 'a6estado', 'a6link', 'a7estado', 'a7link', 'a8estado', 'a8link', 'a9estado', 'a9link', 'a10estado', 'a10link', 'a11estado', 'a11link', 'a12estado', 'a12link', 'a13estado', 'a13link', 'a14estado', 'a14link', 'a15estado', 'a15link', 'a16estado', 'a16link', 'insignias_ganadas')
