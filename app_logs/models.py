from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m',blank=True,null=True)

# class Watching(models.Model):
#     slug = models.CharField(max_length=150)
#     time = models.DateTimeField(blank=True,null= True)
