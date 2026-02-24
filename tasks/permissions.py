from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    """
    - Admin can access any object
    - Regular user can access only their own object
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user == request.user