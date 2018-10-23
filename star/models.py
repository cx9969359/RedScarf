from django.db import models


# Create your models here.
class Check(models.Model):
    title = models.CharField(max_length=128, default='')
