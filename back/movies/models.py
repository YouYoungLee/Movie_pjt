from django.conf import settings
from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_data = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    genre = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=200)
    actor = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    runnig_time = models.CharField(max_length=150)
    video = models.CharField(max_length=150)

class Review(models.Model):
    content = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Global_Movie(models.Model):
    title = models.CharField(max_length=100)
    release_data = models.DateField()
    vote_average = models.FloatField()
    overview = models.TextField()
    genre = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=200)
    actor = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    runnig_time = models.CharField(max_length=150)
    video = models.CharField(max_length=150)