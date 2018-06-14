from rest_framework import serializers
from copatic.models.fase import Fase

class FaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fase
        fields = ('id', 'nombre', 'estado')
