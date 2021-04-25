# from django.db import models
from djongo import models


class Member(models.Model):
    signup = models.DateTimeField()
    points = models.IntegerField()
    name = models.CharField(max_length=15)
