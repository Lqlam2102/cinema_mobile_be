from django.db import models

# Create your models here.
from app_logs.models import User


class Favorite(models.Model):
    slug = models.CharField(max_length=150)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.JSONField(blank=True,null=True)

class TimeMovies(models.Model):
    slug = models.CharField(max_length=150)
    time = models.FloatField(default=0,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    chap = models.SmallIntegerField(blank=True,null=True)
