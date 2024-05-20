from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='moderator').exists()

class IsModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or (request.user and request.user.is_staff)

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj == request.user

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
