from django.http import JsonResponse
from chat.functions.rooms import give_rooms, create_room_for_name, delete_room_for_name
import json
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from chat.functions.users import check_user_in_db, create_user, give_users
from autheticated import IsAuthenticatedWithAddLastLogging


def login(request):
    if request.method == "POST":
        try:
            user = check_user_in_db(json.loads(request.body)["username"])
            if user is not None:
                token = Token.objects.get(user=user)
                return JsonResponse({'token': token.key}, status=200)
            return JsonResponse({"error": "login_error_no_have_user"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)


def registration(request):
    if request.method == "POST":
        body_req_js = json.loads(request.body)
        try:
            if len(json.loads(request.body)["username"]) > 0:
                if len(json.loads(request.body)["password"]) > 0:
                    if check_user_in_db(json.loads(request.body)["username"]) is None:
                        return JsonResponse({"token": Token.objects.create(user=create_user(body_req_js)).key})
                    else:
                        return JsonResponse({"error": "registration_error_already_have_user"}, status=200)
                else:
                    return JsonResponse({"error": "registration_error_password_must_be_not_empty"}, status=200)
            else:
                return JsonResponse({"error": "registration_error_username_must_be_not_empty"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)


class GetRooms(APIView):
    check_auth = IsAuthenticatedWithAddLastLogging()

    def get(self, request):
        self.check_auth.has_permission(request, self)
        return JsonResponse(give_rooms(request.user.username), status=200)


class GetUsers(APIView):
    check_auth = IsAuthenticatedWithAddLastLogging()

    def get(self, request):
        self.check_auth.has_permission(request, self)
        #return JsonResponse(give_users(), status=200)
        try:
            room = give_users(request.GET.get("id"))
            if room is not None:
                return JsonResponse({"users": room}, status=200)
            else:
                return JsonResponse({"error": "delete_room_error_no_have_room_with_this_id"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)


class CreateRoom(APIView):
    check_auth = IsAuthenticatedWithAddLastLogging()

    def get(self, request):
        self.check_auth.has_permission(request, self)
        try:
            room = create_room_for_name(request.GET.get("name"))
            if room is not None:
                return JsonResponse({"room": room}, status=200)
            else:
                return JsonResponse({"error": "create_room_error_already_have_room_with_this_name"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)


class DeleteRoom(APIView):
    check_auth = IsAuthenticatedWithAddLastLogging()

    def get(self, request):
        self.check_auth.has_permission(request, self)
        try:
            room = delete_room_for_name(request.GET.get("id"))
            if room is not None:
                return JsonResponse({"room": room}, status=200)
            else:
                return JsonResponse({"error": "delete_room_error_no_have_room_with_this_id"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)