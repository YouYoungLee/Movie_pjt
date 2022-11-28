from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User
from .serializers import UserListSerializer, UserSerializer

# Create your views here.

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def login(request, user_name):
    user = get_object_or_404(User, username=user_name)
    serializer = UserListSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)