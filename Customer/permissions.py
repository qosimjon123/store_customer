import logging

from rest_framework.permissions import IsAdminUser as BaseIsAdminUser
logging.basicConfig(level=logging.INFO)

class IsAdminUser(BaseIsAdminUser):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):

        return bool(request.user and request.user.role_id == 4)


