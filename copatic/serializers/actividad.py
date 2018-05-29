from rest_framework import serializers
from copatic.models.actividad import Actividad

class ActividadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actividad
        fields = ('id', 'titulo', 'fase', 'puntos', 'descripcion', 'insignias')
