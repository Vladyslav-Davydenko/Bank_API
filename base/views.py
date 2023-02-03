from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Bank


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET", "profiles"},
        {"GET", "profiles/name"},
        {"GET", "bank"},
        {"GET", "bank/name"},
    ]
    return Response(routes)
