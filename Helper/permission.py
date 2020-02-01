from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.__str__)
        return obj.owner.pk == request.user.pk
