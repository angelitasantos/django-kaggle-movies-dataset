from django.db import models
from uuid import uuid4

# Create your models here.
class Movies(models.Model):
    id_movie = models.UUIDField(primary_key=True, default=uuid4, editable=False)
        
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    year = models.IntegerField()
    users_rating = models.FloatField()
    votes = models.IntegerField()

    metascore = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    countries = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    actors = models.TextField()

    genre = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    directors = models.TextField(max_length=255)
    runtime = models.CharField(max_length=255)
    imdb_url = models.CharField(max_length=255)