from django.contrib.auth import get_user_model
from movies.models import Movie
from rest_framework import serializers

from .models import Message, Room

# from accounts.models import User
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('nickname',)

class RoomListSerializer(serializers.ModelSerializer):
    user1_nickname = serializers.CharField(source="user1.nickname",read_only=True)
    user1_gender = serializers.CharField(source="user1.gender",read_only=True)
    user1_region = serializers.CharField(source="user1.region",read_only=True)

    user2_nickname = serializers.CharField(source="user2.nickname",read_only=True)
    user2_gender = serializers.CharField(source="user2.gender",read_only=True)
    user2_region = serializers.CharField(source="user2.region",read_only=True)
    class Meta:
        model = Room
        fields = '__all__'
        read_only_fields = ('article','user1',)

class MessageListSerializer(serializers.ModelSerializer):
    
    user_nickname = serializers.CharField(source="user.nickname",read_only=True)
    user_gender = serializers.CharField(source="user.gender",read_only=True)
    user_region = serializers.CharField(source="user.region",read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('room','user',)