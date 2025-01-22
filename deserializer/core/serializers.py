from rest_framework import serializers
from . models import Marvel


class MarvelSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=50)
    heroic_name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Marvel.objects.create(**validated_data)