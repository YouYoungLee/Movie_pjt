from django.urls import path

from . import views

urlpatterns = [
    path('create/<int:article_pk>/',views.roomcreate),
    path('index/',views.roomindex),
    path('<int:user1_pk>/<int:user2_pk>/',views.Roomdetail),
    path('<int:room_pk>/message/create/',views.message_create),
    path('room_message/<int:room_pk>/',views.message_comments),
    path('<int:room_pk>/',views.Roomdetail2),
]