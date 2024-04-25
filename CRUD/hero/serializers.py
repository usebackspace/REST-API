from rest_framework import serializers
from .models import Hero


class HeroSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    heroic_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Hero.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.heroic_name = validated_data.get('heroic_name',instance.heroic_name)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance