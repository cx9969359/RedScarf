from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128, default='')
    password = models.CharField(max_length=256, default='')


class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token = models.CharField(max_length=256, default='')


class Check(models.Model):
    title = models.CharField(max_length=128, default='')
