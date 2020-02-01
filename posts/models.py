from django.db import models
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, default='no title')
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
