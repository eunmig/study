from rest_framework import serializers
from .models import User

from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from .adapters import CustomAccountAdapter

class CustomRegisterSerializer(RegisterSerializer):
    salary = serializers.IntegerField(required=True)

    def get_adapter(self):
        return CustomAccountAdapter()

    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['salary'] = self.validated_data.get('salary', '')
        return cleaned_data
    

class UserProfileSerializer(serializers.ModelSerializer):
    salary = serializers.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'salary']