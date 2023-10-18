from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Music
from .serializers import MusicListSerializer, MusicSerializer


@api_view(['GET', 'POST'])
def music_list(request):
    if request.method == 'GET':
        Musics = Music.objects.all()
        serializer = MusicListSerializer(Musics, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def music_detail(request, article_pk):
    music = Music.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
