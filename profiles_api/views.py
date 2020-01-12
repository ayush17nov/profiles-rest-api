from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from profiles_api import serializers, models, permissions


# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to index Page</h1>")

class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returns a list of API view features"""
        api_view = [
            "will be used methods get post patch put delete",
            "new more data",
            "first api view content",
        ]

        return Response({"message":"First API view", "api_view":api_view})

    def post(self, request):
        """create a new object with the data posted"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}!"
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """handle partial update of an object"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({"method": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return hello message"""

        a_viewset = [
            'uses actions (list, create, retrieve, update, partial update, and delete )',
            'Automatically maps to URLs using routers',
            'Provide more functionality with less code'
        ]

        return Response({"message": "Hello!!", "a_viewset":a_viewset})

    def create(self, request):
        """create new object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """return a object by id"""
        return Response({"http_method": "Retrieve"})

    def update(self, request, pk=None):
        """update an object by id provided"""
        return Response({"http_method": "UPDATE"})

    def partial_update(self, request, pk=None):
        """update an object partially"""
        return Response({"http_method": "PATCH"})

    def destroy(self, request, pk=None):
        """delete and object supplied"""
        return Response({"http_method": "DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating objects"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', )