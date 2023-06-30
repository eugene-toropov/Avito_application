from rest_framework import permissions

from users.models import UserRoles


class IsOwner(permissions.BasePermission):
    message = 'Обновлять или удалять объявление может только его создатель!'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdmin(permissions.BasePermission):
    message = 'Только администратор имеет доступ!'

    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN
