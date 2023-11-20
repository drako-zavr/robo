# from rest_framework.permissions import IsAuthenticated
# from rest_framework_api_key.permissions import HasAPIKey


# class HasApiKeyOrIsAuthenticated(HasAPIKey):
#     def has_permission(self, request, view):
#         return super().has_permission(request, view) or bool(
#             request.user and request.user.is_authenticated
#         )
from rest_framework.permissions import BasePermission
from django.conf import settings

class BlockCORS(BasePermission):
    def has_permission(self, request, view) -> bool:
        return (
            settings.DEBUG
            or str(request.META.get("HTTP_REFERER")).find(settings.SITE_DOMAIN)
            > -1
        )
