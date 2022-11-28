from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.conf import settings
from rest_framework import serializers

from .models import User


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=30)
    region = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=30)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['gender'] = self.validated_data.get('gender', '')
        data_dict['region'] = self.validated_data.get('region', '')
        data_dict['name'] = self.validated_data.get('name', '')
        return data_dict

class UserSerializer(UserDetailsSerializer):
    # def create(self, data):
    #     user = User.objects.create_user(
    #         username = data['username'],
    #         nickname = data['nickname'],
    #         name = data['name'],
    #         password = data['password'],
    #         gender = data['gender'],
    #         region = data['region'],
    #     )
    #     return user
    class Meta(UserDetailsSerializer):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'username', 'name', 'password', 'gender', 'region',)

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nickname','gender','region','id')