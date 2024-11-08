from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        """Authenticated users only can see list view."""
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """Read permissions are allowed to any request,
         so we'll always allow GET, HEAD, or OPTIONS request."""
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only allowed to the author of the post.
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
