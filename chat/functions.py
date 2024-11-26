from django.contrib.auth.models import User


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


def give_users():
    return {"users": list(User.objects.all().values("username", "last_login"))}