from rest_framework import serializers
from .models import Music


class MusicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
