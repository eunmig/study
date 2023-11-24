from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserDataSerializer, CarSerializer
import requests
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import User, Car


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


@api_view(['GET'])
def get_carinfo(request):
    cars = get_list_or_404(Car)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_my_cars(request, salary_level):
    if salary_level == 5:
        cars = Car.objects.all()
    else:
        cars = get_list_or_404(Car, salary_level=salary_level)
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_one_car(request, car_pk):
    car = get_object_or_404(Car, pk=car_pk)
    serializer = CarSerializer(car)
    return Response(serializer.data)