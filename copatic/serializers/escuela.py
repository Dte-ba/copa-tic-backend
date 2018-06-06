from rest_framework import serializers
from copatic.models.escuela import Escuela
from rest_framework_json_api.relations import ResourceRelatedField

class EscuelaSerializer(serializers.ModelSerializer):
    equipos = ResourceRelatedField(many=True, read_only=True, required=False)

    included_serializers = {
        'equipos': 'copatic.serializers.equipo.EquipoSerializer'
    }

    class Meta:
        model = Escuela
        fields = ('id', 'nombre', 'localidad', 'latitud', 'longitud', 'equipos')

    class JSONAPIMeta:
        included_resources = ['equipos']
