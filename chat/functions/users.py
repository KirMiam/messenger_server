from django.contrib.auth.models import User
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from datetime import datetime
import pytz


def check_user_in_db(body):
    if len(User.objects.filter(username=body)) > 0:
        return User.objects.get(username=body)
    else:
        return None


def create_user(body):
    user = User.objects.create_user(body["username"], (body["username"] + "@gmail.com"),
                                    body['password'])
    user.save()
    return user


def give_users(room_id):
    return {"users": list(User.objects.all().values("username", "last_login"))}


@database_sync_to_async
def get_user_by_token(token_key):
    try:
        return Token.objects.get(key=token_key).user
    except Token.DoesNotExist:
        return None


@database_sync_to_async
def last_login_save(name):
    user = User.objects.get(username=name)
    user.last_login = datetime.now().replace(tzinfo=pytz.utc)
    user.save(update_fields=['last_login'])
