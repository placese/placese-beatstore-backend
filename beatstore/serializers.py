from rest_framework.serializers import ModelSerializer

from beatstore.models import Beat


class BeatSerializer(ModelSerializer):
    class Meta:
        model = Beat
        fields = '__all__'
