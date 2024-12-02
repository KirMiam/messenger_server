from django.http import JsonResponse
from chat.functions.rooms import give_rooms
from rest_framework.views import APIView
from autheticated import IsAdminUserWithAddLastLogging


class GetRoomsAdmin(APIView):
    check_auth = IsAdminUserWithAddLastLogging()

    def get(self, request):
        if self.check_auth.has_permission(request, self) is True:
            return JsonResponse(give_rooms(), status=200)
        else:
            return JsonResponse({"error": "Unauthorized"}, status=401)