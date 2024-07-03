from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Category, Post, Comment
from .serializers import CategorySerializer, PostListSerializer, PostSerializer, CommentSerializer


# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        Categories = get_list_or_404(Category)
        serializer = CategorySerializer(Categories, many=True)
        return Response(serializer.data)

        
@api_view(['POST'])
@permission_classes([IsAdminUser])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_create(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(category=category, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['DELETE', 'PUT'])
def post_UD(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
def post_del(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.delete()
    data = {
        'delete': f'데이터 {post_pk}번 글이 삭제되었습니다.',
    }
    return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data) 