from django.db import models
from accounts.models import User


class Notify(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	is_read = models.BooleanField(default=False)
	body = models.TextField(max_length=1000)
	link = models.CharField(max_length=255)

	class Meta:
		db_table = 'notify'
