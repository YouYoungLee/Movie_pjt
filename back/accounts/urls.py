from django.urls import include, path
from rest_framework import urls

from . import views

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('<str:user_name>/', views.login)
]