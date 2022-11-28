from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect, render)
from django.views.decorators.http import require_http_methods, require_POST
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from movies.models import Movie

from .models import Article, Comment
from .serializers import ArticleListSerializer, CommentListSerializer


# Create your views here.
@api_view(['POST'])
def articlecreate(request):
    movie_title = request.data.get('movie_title')
    movie = get_object_or_404(Movie, pk=movie_title)
    serializer = ArticleListSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_title=movie,user=request.user)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def articleindex(request):
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def articledetail(request, article_pk):
    article = get_object_or_404(Article,pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        movie_title = request.data.get('movie_title')
        movie = get_object_or_404(Movie,pk=movie_title)

        serializer = ArticleListSerializer(instance=article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie_title=movie,user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else: 
        article.delete()
        return Response(data='delete success',status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def comment_create(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = CommentListSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article,user=request.user)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def article_comments(request,article_pk):
    comments = get_list_or_404(Comment,article_id=article_pk)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['PUT','DELETE'])
def comment_update_delete(request,article_pk,comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        comment_serializer = CommentListSerializer(instance=comment,data=request.data)
        if comment_serializer.is_valid(raise_exception=True):
            comment_serializer.save(article=article,user=request.user)
            return Response(comment_serializer.data,status=status.HTTP_201_CREATED)

    else:
        comment.delete()
        return Response(data='delete success',status=status.HTTP_204_NO_CONTENT)    
