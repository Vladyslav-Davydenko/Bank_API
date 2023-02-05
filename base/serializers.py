from rest_framework.serializers import ModelSerializer
from .models import Profile, Bank

class BankSerializer(ModelSerializer):
    class Meta():
        model = Bank
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    bank = BankSerializer()
    class Meta():
        model = Profile
        fields = '__all__'
