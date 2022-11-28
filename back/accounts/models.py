from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.



class User(AbstractUser):
    nickname = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    region = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
