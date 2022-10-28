from email.policy import default
from turtle import title
from datetime import datetime
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    title = models.CharField(max_length = 400)
    date_released = models.DateField()
    likes = models.IntegerField()
    artisteid = models.IntegerField()

    def __str__(self):
        return self.title
class Lyric(models.Model):
    Song = models.ForeignKey(Song, on_delete = models.CASCADE)
    context = models.CharField(max_length = 4000)
    songid = models.IntegerField()

    def __str__(self):
        return self.context