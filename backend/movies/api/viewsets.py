from rest_framework import viewsets
from movies.api import serializers
from movies import models

class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MoviesSerializer
    queryset = models.Movies.objects.all()