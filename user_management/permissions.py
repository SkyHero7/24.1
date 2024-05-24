from rest_framework.permissions import BasePermission

class IsModeratorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Модераторы').exists():
            return True
        return request.method in ('GET', 'HEAD', 'OPTIONS')

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.user == request.user