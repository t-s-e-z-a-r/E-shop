from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    first_name = models.CharField(max_length=255, default=0)
    last_name = models.CharField(max_length=255, default=0)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(default=0)

