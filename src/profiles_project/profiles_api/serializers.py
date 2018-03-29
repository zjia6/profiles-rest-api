from rest_framework import serializers


class HellowSerializer(serializers.Serializer):
    """Serializes a name field for the testing APIView"""

    name = serializers.CharField(max_length=10)
