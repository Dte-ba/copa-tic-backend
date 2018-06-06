from rest_framework import serializers
from copatic.models.actividad import Actividad
from rest_framework_json_api.relations import ResourceRelatedField

class ActividadSerializer(serializers.ModelSerializer):

    insignias =  ResourceRelatedField(many=True, read_only=True, required=False)

    included_serializers = {
        'insignias': 'copatic.serializers.insignia.InsigniaSerializer'
    }

    class Meta:
        model = Actividad
        fields = ('id', 'titulo', 'fase', 'puntos', 'descripcion', 'insignias')

    class JSONAPIMeta:
        included_resources = ['insignias']
