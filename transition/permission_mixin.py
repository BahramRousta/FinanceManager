from rest_framework import permissions


class IsOwnerTransition(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
