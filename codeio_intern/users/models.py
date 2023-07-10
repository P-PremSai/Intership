from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=200, unique = True,null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

   

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
