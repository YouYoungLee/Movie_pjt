from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Global_Movie, Movie, Review

User = get_user_model()

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.nickname",read_only=True)

    class Meta:
        model = Review
        fields = ('content','user')
        read_only_fields = ('movie',)

class ReviewsSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('nickname',)
    user_nickname = serializers.CharField(source="user.nickname",read_only=True)
    user_gender = serializers.CharField(source="user.gender",read_only=True)
    user_region = serializers.CharField(source="user.region",read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class GlobalMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Global_Movie
        fields = '__all__'
