from rest_framework import serializers
from .models import User

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
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
    

# class UserProfileSerializer(serializers.ModelSerializer):
#     salary = serializers.IntegerField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'first_name', 'last_name', 'salary']

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  '__all__'

