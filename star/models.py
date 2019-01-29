from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, default='')
    password = models.CharField(max_length=256, default='')
    created_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, auto_now_add=False)


class TokenObject(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=256, default='')
    created_time = models.DateTimeField(auto_now=False, auto_now_add=True)


class Check(models.Model):
    title = models.CharField(max_length=128, default='')
