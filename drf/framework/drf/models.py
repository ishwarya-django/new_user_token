from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=80,unique=True)
    password=models.CharField(max_length=50)
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =[]

class Transformer(models.Model):
    topic= models.CharField(max_length=20)
    text=models.CharField(max_length=50)
    title=models.CharField(max_length=80,unique=True)
    content=models.CharField(max_length=50)
    age=models.IntegerField()


class Student(models.Model):
    firstname= models.CharField(max_length=20)
    lastname=models.CharField(max_length=50)
   
    std=models.IntegerField()
    section=models.IntegerField()
