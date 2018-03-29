from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'User HTTP method as function',
            'It is similar to tradmtional Django view',
            'Gives most control over the logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
