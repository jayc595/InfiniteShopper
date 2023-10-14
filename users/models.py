from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


class User(AbstractBaseUser):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=50)