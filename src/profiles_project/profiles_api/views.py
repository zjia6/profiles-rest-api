from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers


# Create your views here.

class HellowViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class = serializers.HellowSerializer

    def list(sefl, requet):
        """Return a hellow message."""

        a_viewset = [
            'uses action (list, create, retrieve, update, partial_update)',
            'automatically maps to URLs URLs Routers',
            'priveds more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""

        serializer = serializers.HellowSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting an object by its ID."""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles updating an object by its ID."""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an object by its ID."""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object."""
        return Response({'http_method': 'DELETE'})


class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HellowSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'User HTTP method as function',
            'It is similar to tradmtional Django view',
            'Gives most control over the logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with name provided."""

        serializer = serializers.HellowSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)

            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an objet."""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """Patch request, only updates field provided in the request."""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Deletes an object."""

        return Response({'method': 'delete'})
