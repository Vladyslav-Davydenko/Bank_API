from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile, Bank
from .serializers import ProfileSerializer, BankSerializer


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"GET", "profiles"},
        {"GET", "profiles/name"},
        {"GET", "bank"},
        {"GET", "bank/name"},
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getListOfProfiles(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        profile = Profile.objects.create(
            name = request.data['name'],
            surname = request.data['surname'],
        )
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def getListOfBanks(request):
    if request.method == 'GET':
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        banks = Bank.objects.create(
            name = request.data['name'],
            commission = request.data['commission'],
        )
        serializer = BankSerializer(banks, many=False)
        return Response(serializer.data)