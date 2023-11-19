from rest_framework import serializers
from .models import exchange

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = exchange
        fields = '__all__'