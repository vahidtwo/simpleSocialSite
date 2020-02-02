from rest_framework.permissions import BasePermission
from chanel.models import Chanel
from posts.models import Post


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj._meta is Post._meta:
            return True
        elif obj._meta is Chanel._meta:
            return obj.owner.pk == request.user.pk


class IsAuthorOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj._meta is Post._meta:
            return obj.author == request.user
        elif obj._meta is Chanel._meta:
            return request.user in obj.author.all()
