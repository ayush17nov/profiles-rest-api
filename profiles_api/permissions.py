from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """allow users to update own profile"""

    def has_object_permission(self, request, views, obj):
        """check user is trying to update own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id