from django.contrib.auth import get_user_model
from rest_framework import serializers

from movies.models import Movie

from .models import Article, Comment

User = get_user_model()

class ArticleListSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname",read_only=True)
    user_gender = serializers.CharField(source="user.gender",read_only=True)
    user_region = serializers.CharField(source="user.region",read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('movie_title','user')

class CommentListSerializer(serializers.ModelSerializer):

    user_nickname = serializers.CharField(source="user.nickname",read_only=True)
    user_gender = serializers.CharField(source="user.gender",read_only=True)
    user_region = serializers.CharField(source="user.region",read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','user')
