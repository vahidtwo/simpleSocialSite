from django.db import models

# Create your models here.
from accounts.models import User
from posts.models import Post


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='for_comment')
    body = models.TextField(max_length=2500)

    class Meta:
        db_table = 'comment'
