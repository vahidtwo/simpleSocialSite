from django.db import models
from django.utils import timezone

from accounts.models import User
from chanel.models import Chanel


class Post(models.Model):
	title = models.CharField(max_length=200, default='no title')
	body = models.TextField()
	chanel = models.ForeignKey(Chanel, on_delete=models.CASCADE)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = "post"
