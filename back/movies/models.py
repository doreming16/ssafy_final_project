from django.db import models

# Create your models here.
class Movie:
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    backdrop_path = models.TextField()
    poster_path = models.TextField()

class Genre:
    name = models.CharField(max_length=6)