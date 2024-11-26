from django.http import JsonResponse
from rooms.rooms import give_rooms, create_room_for_name, delete_room_for_name
import json
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chat.functions import check_user_in_db, create_user, give_users
from django.contrib.auth.models import User


# def test_func(request):
#     tokens = []
#     users_id = []
#     users = []
#     list_of_tokens = list(Token.objects.all())
#     for i in iter(list_of_tokens):
#         tokens.append(i)
#     for i in tokens:
#         users_id.append(Token.objects.get(key=i).user_id)
#     for i in users_id:
#         users.append(User.objects.get(id=i))
#     print("------")
#     print(users)
#     print("------")
#     a = {}
#     return JsonResponse(a)

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
    check_auth = IsAuthenticated()

    def get(self, request):
        return JsonResponse(give_rooms(), status=200)


class GetUsers(APIView):
    check_auth = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse(give_users(), status=200)



class CreateRoom(APIView):
    check_auth = (IsAuthenticated,)

    def post(self, request):
        try:
            name_of_room = json.loads(request.body)["name"]
            if len(name_of_room) > 0:
                room = create_room_for_name(name_of_room)
                if room is not None:
                    return JsonResponse({"room": room}, status=200)
                else:
                    return JsonResponse({"error": "create_room_error_already_have_room_with_this_name"}, status=200)
            else:
                return JsonResponse({"error": "create_room_error_name_must_be_not_empty"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)


class DeleteRoom(APIView):
    check_auth = (IsAuthenticated,)

    def post(self, request):
        try:
            name_of_room = json.loads(request.body)["name"]
            if len(name_of_room) > 0:
                room = delete_room_for_name(name_of_room)
                if room is not None:
                    return JsonResponse({"room": room}, status=200)
                else:
                    return JsonResponse({"error": "delete_room_error_no_have_room_with_this_name"}, status=200)
            else:
                return JsonResponse({"error": "delete_room_error_name_must_be_not_empty"}, status=200)
        except:
            return JsonResponse({"error": "BadRequest"}, status=400)