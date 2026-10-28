from rest_framework.permissions import BasePermission
class Is_Superuser_or_Staff(BasePermission):
    
    def has_permission(self, request, view):
       return bool(
           request.user and
           request.user.is_authenticated and
           request.user.is_staff or request.user.is_superuser
       )

