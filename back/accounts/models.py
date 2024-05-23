from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class UserInfo(models.Model):
    isSpecial = models.BooleanField(default=False)
    gender = models.TextField()
    era = models.TextField()
    favorite_genre = models.JSONField(default=list, blank=True)
    viewing_environment = models.TextField()
    birthday = models.DateField()