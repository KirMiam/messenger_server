from datetime import datetime, timezone
from rest_framework.permissions import IsAuthenticated
import pytz
from datetime import datetime


class IsAuthenticatedWithAddLastLogging(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            user = request.user
            user.last_login = datetime.now().replace(tzinfo=pytz.utc)
            print(user.last_login)
            user.save(update_fields=['last_login'])
        return request.user and request.user.is_authenticated