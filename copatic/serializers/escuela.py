from rest_framework import serializers
from copatic.models.escuela import Escuela

class EscuelaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Escuela
        fields = ('id', 'nombre', 'localidad', 'latitud', 'longitud')
