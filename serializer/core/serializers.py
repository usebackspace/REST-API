from rest_framework import serializers

class MarvelSerializer(serializers.Serializer):
    f_name = serializers.CharField(max_length=50)
    heroic_name = serializers.CharField(max_length=50)