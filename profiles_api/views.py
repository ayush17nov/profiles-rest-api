from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class HelloApiView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """returns a list of API view features"""
        api_view = [
            "will be used methods get post patch put delete",
            "new more data",
            "first api view content",
        ]

        return Response({"message":"First API view", "api_view":api_view})