from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
    
class IsManager(permissions.BasePermission):
    """
    Custom permission to only allow access to Manager users.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Manager').exists()

class IsEmployee(permissions.BasePermission):
    """
    Custom permission to only allow access to Employee users.
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Employee').exists()