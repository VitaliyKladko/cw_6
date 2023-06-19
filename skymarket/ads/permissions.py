from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Вы не владелец"

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.author == user:
            return True
        return False
