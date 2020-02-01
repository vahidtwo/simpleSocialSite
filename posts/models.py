from django.db import models
from chanel.models import Chanel


class Post(models.Model):
    title = models.CharField(max_length=200, default='no title')
    body = models.TextField()
    owner = models.ForeignKey(Chanel, on_delete=models.CASCADE)

    class Meta:
        db_table = "post"
