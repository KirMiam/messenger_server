from rest_framework.permissions import IsAuthenticated, IsAdminUser
from datetime import datetime
import pytz


class IsAuthenticatedWithAddLastLogging(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user = request.user
            user.last_login = datetime.now().replace(tzinfo=pytz.utc)
            user.save(update_fields=['last_login'])
        return request.user and request.user.is_authenticated


class IsAdminUserWithAddLastLogging(IsAdminUser):
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            user = request.user
            user.last_login = datetime.now().replace(tzinfo=pytz.utc)
            user.save(update_fields=['last_login'])
        return bool(request.user and request.user.is_staff)
