from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Category, Post, Comment
from accounts.serializers import UserPostSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user_data = UserPostSerializer(source='user', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user',)

class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'category')

class PostSerializer(serializers.ModelSerializer):
    user_data = UserPostSerializer(source='user', read_only=True)
    category = CategorySerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)

