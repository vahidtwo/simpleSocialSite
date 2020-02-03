from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
	def create_user(self, first_name, last_name, phone_number, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
		)
		user.first_name = first_name
		user.username = username
		user.last_name = last_name
		user.phone_number = phone_number
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, first_name, last_name, phone_number, email, password):
		user = self.create_user(
			email=email,
			first_name=first_name,
			last_name=last_name,
			phone_number=phone_number,
			password=password,
		)
		user.admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(
		max_length=255,
		unique=True,
	)
	username = models.CharField(max_length=200, unique=True)
	active = models.BooleanField(default=True)
	admin = models.BooleanField(default=False)  # a superuser
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=13, unique=True)
	city = models.CharField(max_length=30, null=True)
	country = models.CharField(max_length=30, null=True)
	picture = models.ImageField(upload_to='profile/', max_length=1000, null=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

	def get_full_name(self):
		return str(self.first_name) + ' ' + str(self.last_name)

	def get_username(self):
		return self.username

	def __str__(self):
		return self.get_full_name()

	# def has_perm(self, perm, obj=None):
	#     """Does the user have a specific permission?"""
	#     return True

	objects = UserManager()
