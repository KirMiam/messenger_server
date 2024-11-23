from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


def check_user_in_db(body):
    user = authenticate(username=body["username"], password=body['password'])
    return user


def create_user(body):
    user = User.objects.create_user(body["username"], (body["username"] + "@gmail.com"),
                                    body['password'])
    user.save()
    return user
