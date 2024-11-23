from django.http import JsonResponse
from rooms.rooms import give_rooms, create_room_for_name
import json
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from chat.functions import check_user_in_db, create_user
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
        user = check_user_in_db(json.loads(request.body))
        if user is not None:
            token = Token.objects.get(user=user)
            return JsonResponse({'token': token.key}, status=200)
        return JsonResponse({"error": "login_error_no_have_user"}, status=200)


def registration(request):
    if request.method == "POST":
        body_req_js = json.loads(request.body)
        if check_user_in_db(json.loads(request.body)) is None:
            return JsonResponse({"token": Token.objects.create(user=create_user(body_req_js)).key})
        else:
            return JsonResponse({"error": "registration_error_already_have_user"}, status=200)


class Rooms(APIView):
    check_auth = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse(give_rooms(), status=200)


class CreateRoom(APIView):
    check_auth = (IsAuthenticated,)

    def post(self, request):
        return JsonResponse({"room": create_room_for_name(json.loads(request.body)["name"])}, status=200)
