from rest_framework import permissions


class UserOwnObjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.method == 'GET':
                return True

        return obj.id == request.user.id


class UserOwnStatusPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.method == 'GET':
                return True

        return obj.user.id == request.user.id
