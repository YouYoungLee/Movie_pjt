# Create your views here.
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)
from django.views.decorators.http import require_http_methods, require_POST
from movies.models import Movie
from community.models import Article

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Message, Room

from .serializers import RoomListSerializer,MessageListSerializer


# Create your views here.
@api_view(['POST'])
def roomcreate(request,article_pk):
    user22={'user2':article_pk}
    serializer = RoomListSerializer(data=user22)

    if serializer.is_valid(raise_exception=True):
        serializer.save(user1=request.user)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def roomindex(request):
    articles = get_list_or_404(Room)
    serializer = RoomListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def Roomdetail2(request,room_pk):
    room = get_object_or_404(Room,pk=room_pk)
    serializer = RoomListSerializer(room)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def Roomdetail(request, user1_pk,user2_pk):
    room = get_object_or_404(Room,user1_id=user1_pk,user2=user2_pk)
    serializer = RoomListSerializer(room)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def message_create(request,room_pk):
    room = get_object_or_404(Room,pk=room_pk)
    serializer = MessageListSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(room=room,user=request.user)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def message_comments(request,room_pk):
    message = get_list_or_404(Message,room_id=room_pk)
    serializer = MessageListSerializer(message, many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

