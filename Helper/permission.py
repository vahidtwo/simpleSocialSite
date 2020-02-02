from rest_framework.permissions import BasePermission
from chanel.models import Chanel
from comment.models import Comment
from notify.models import Notify
from posts.models import Post


class IsOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj._meta is Chanel._meta or obj._meta is Comment._meta:
			return obj.owner.pk == request.user.pk
		elif obj._meta is Notify._meta:
			return request.user == obj.user


class IsAuthorOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		if obj._meta is Post._meta:
			return obj.author == request.user or obj.owner == request.user
		elif obj._meta is Chanel._meta:
			return request.user in obj.author.all() or obj.owner == request.user


class IsChanelOwner(BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user
