from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Profile, Bank

class BankSerializer(ModelSerializer):
    users_count = SerializerMethodField(read_only=True)
    class Meta():
        model = Bank
        fields = '__all__'


    def get_users_count(self, obj):
        count = obj.profile_set.count()
        return count

class ProfileSerializer(ModelSerializer):
    bank = BankSerializer()
    class Meta():
        model = Profile
        fields = ['id', 'name', 'surname', 'balance', 'card', 'bank']
