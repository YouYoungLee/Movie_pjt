from django.urls import path

from . import views

urlpatterns = [
    path('create/',views.articlecreate),
    path('index/',views.articleindex),
    path('<int:article_pk>/',views.articledetail),
    path('<int:article_pk>/comments/create/',views.comment_create),
    path('article_comments/<int:article_pk>/',views.article_comments),
    path('<int:article_pk>/comments/<int:comment_pk>/update_delete/',views.comment_update_delete),
]  
