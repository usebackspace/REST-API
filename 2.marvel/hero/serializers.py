from rest_framework import serializers
from . models import Hero

class HeroSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    heroic_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)