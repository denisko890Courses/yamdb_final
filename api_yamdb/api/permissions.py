from rest_framework import permissions

from users.models import User


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        self.message = 'Для доступа необходима авторизация'
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        self.message = 'Возможность изменять информацию есть только у автора'
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or request.user.is_admin
            or request.user.is_moderator)


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and request.user.role == User.ADMIN)
        )
