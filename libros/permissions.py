from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permite solo lectura a usuarios normales.
    Los Admins pueden realizar cualquier operación.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True  # GET, HEAD, OPTIONS siempre permitidos
        return request.user and request.user.is_staff
