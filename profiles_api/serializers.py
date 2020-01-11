from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name field for testing on API-view"""
    name = serializers.CharField(max_length=10)