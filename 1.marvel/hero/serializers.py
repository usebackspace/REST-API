from rest_framework import serializers

class HeroSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    heroic_name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)