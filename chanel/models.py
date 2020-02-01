from django.db import models
from accounts.models import User


class Chanel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    author = models.ManyToManyField(User, related_name='author')
    description = models.TextField(max_length=2500)
    identifier = models.CharField(unique=True, max_length=100)

    class Meta:
        db_table = "chanel"
