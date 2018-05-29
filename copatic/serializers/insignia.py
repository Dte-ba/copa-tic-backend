from rest_framework import serializers
from copatic.models.insignia import Insignia

class InsigniaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actividad
        fields = ('id', 'nombre')
