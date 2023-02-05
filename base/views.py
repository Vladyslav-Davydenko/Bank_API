from django.shortcuts import render
from django.http import JsonResponse
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


#Profile
class ProfileDetails(APIView):
    def get_object(self, id):
        try:
            return Profile.objects.get(id=id)
        except Profile.DoesNotExist:
            raise JsonResponse("Profile does not exist")
    
    def get(self, request, id):
        profile = self.get_object(id)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

    
    def post(self, request, id):
        pass


    def patch(self, request, id):
        profile = self.get_object(id)

        if profile.id == request.data['id']:
            profile.balance += request.data['balance']
            profile.save()
            serializer = ProfileSerializer(profile, many=False)
            return Response(serializer.data)
        else:
            try:
                transfer_to = self.get_object(request.data["id"])
                if profile.bank.commission == 0:
                    transfer_to.balance += request.data['balance']
                else:
                    transfer_to.balance += (request.data['balance'] - (request.data['balance'] / profile.bank.commission))
                profile.balance -= request.data['balance']
                profile.save()
                transfer_to.save()
                serializer = ProfileSerializer(profile, many=False)
                return Response(serializer.data)
            except Profile.DoesNotExist:
                raise JsonResponse("Can not transfer to user that is not exist")
    

    def delete(self, request, id):
        profile = self.get_object(id)
        profile.delete()
        return Response("Profile was deleted")


#Bank
class BankDetails(APIView):
    def get_object(self, name):
        try:
            return Bank.objects.get(name=name)
        except Bank.DoesNotExist:
            raise JsonResponse("Bank does not exist")

    def get(self, request, name):
        bank = self.get_object(name)
        serializer = BankSerializer(bank, many=False)
        return Response(serializer.data)


    def patch(self, request, name):
        bank = self.get_object(name)
        bank.commission = request.data['commission']
        bank.save()
        serializer = BankSerializer(bank, many=False)
        return Response(serializer.data)

    
    def put(self, request, name):
        bank = self.get_object(name)
        bank.name = request.data['name']
        if request.data['commission']:
            bank.commission = request.data['commission']
        bank.save()
        serializer = BankSerializer(bank, many=False)
        return Response(serializer.data)


    def delete(self, request, name):
        bank = self.get_object(name)
        bank.delete()
        return Response("Bank was successfully deleted")