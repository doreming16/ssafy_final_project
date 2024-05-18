from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class UserInfo(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    sex = models.BooleanField()
    age = models.TextField()
    favorite_genre = models.IntegerField()
    viewing_environment = models.TextField()
    birthday = models.DateField()