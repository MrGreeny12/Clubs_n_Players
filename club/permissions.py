from rest_framework.permissions import BasePermission, SAFE_METHODS
from accounts.models import Profile


class IsManagerOrAdminOrReadOnly(BasePermission):
    """
    Даёт доступ только менеджеру или администратору
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            profile = Profile.objects.get(user_id=request.user.id)
            return bool(
                request.method in SAFE_METHODS or
                request.user and request.user.is_authenticated and (profile.role == 'MN')
            )

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        else:
            profile = Profile.objects.get(user_id=request.user.id)
            return bool(
                request.method in SAFE_METHODS or
                request.user and request.user.is_authenticated and (profile.role == 'MN')
            )


class IsPresidentOrAdminOrReadOnly(BasePermission):
    """
    Даёт доступ только президенту или администратору
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            profile = Profile.objects.get(user_id=request.user.id)
            return bool(
                request.method in SAFE_METHODS or
                request.user and request.user.is_authenticated and (profile.role == 'PR')
            )

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        else:
            profile = Profile.objects.get(user_id=request.user.id)
            return bool(
                request.method in SAFE_METHODS or
                request.user and request.user.is_authenticated and (profile.role == 'PR')
            )
