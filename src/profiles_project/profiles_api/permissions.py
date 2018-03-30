from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.id == request.user.id:
            return True

class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status."""

    def has_object_permission(self, request, view, obj):
        """Checks the user is tryign to update theri own status."""

        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.user_profile.id == request.user.id:
            return True
