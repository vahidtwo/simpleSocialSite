from django.db import models

# Create your models here.
from accounts.models import User
from posts.models import Post


class Like(models.Model):
	like_choice = ((1, 'LIKE'), (-1, 'DISLIKE'))
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	value = models.IntegerField(choices=like_choice, default=1)

	class Meta:
		db_table = 'like'