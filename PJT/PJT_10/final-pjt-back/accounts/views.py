from django.shortcuts import render
<<<<<<< HEAD
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserDataSerializer
import requests
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User


# Create your views here.

# @permission_classes([IsAuthenticated])
# class UserProfileView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserProfileSerializer

#     def get_object(self):
#         return self.request.user
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_data(request, username):
    user_data = get_object_or_404(User, username=username)
    serializer = UserDataSerializer(user_data)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_user_datas(request):
    user_data = get_list_or_404(User)
    serializer = UserDataSerializer(user_data, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_profile(request, user_pk):
    user_data = get_object_or_404(User, pk=user_pk)

    # You need to pass the instance and request data to the serializer
    serializer = UserDataSerializer(user_data, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
=======
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer

# Create your views here.

@permission_classes([IsAuthenticated])
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
>>>>>>> 5f1367ace20c3b6af39823011830c3433fb7eb1b
