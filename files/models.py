from django.db import models


class FileModel(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')

	class Meta:
		db_table = 'file'
