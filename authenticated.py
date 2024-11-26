import time

from rest_framework.permissions import IsAuthenticated


class IsAuthenticatedWithAddLastLogging(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user = request.user
            user.last_login = time.time()
            user.save(update_fields=['last_login'])
        return request.user and request.user.is_authenticated