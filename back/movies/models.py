from django.db import models
from accounts.models import User

# Create your models here.
class Movie(models.Model):
    title = models.TextField()
    original_title = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    adult = models.BooleanField()
    # 데이터에 없는 값이 있어서 이 값은 null로 처리해줌
    backdrop_path = models.TextField(null=True)
    poster_path = models.TextField(null=True)

class Genre(models.Model):
    name = models.CharField(max_length=6)

class Review(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()
    content = models.TextField()