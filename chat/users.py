from django.contrib.auth.models import User

def createUser(name, address, password):
    user = User.objects.create_user(name, address, password)
    user.save()