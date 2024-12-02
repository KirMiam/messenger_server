from chat.models import Rooms, Messages, RoomUsers
from channels.db import database_sync_to_async


def create_room_for_name(name):
    room = Rooms()
    if len(Rooms.objects.filter(name=name).values()) == 0:
        room.name = name
        room.save()
        return Rooms.objects.filter(name=name).values()[0]
    else:
        return None


def delete_room_for_name(id_of_room):
    if len(Rooms.objects.filter(id=id_of_room).values()) != 0:
        room = Rooms.objects.filter(id=id_of_room).values()[0]
        #Rooms.objects.get(id=id_of_room).group.clear()
        Rooms.objects.get(id=id_of_room).delete()
        return room
    else:
        return None


def give_rooms(user):
    list_to_return = []
    for i in list(Rooms.objects.all()):
        try:
            if check_user_in_room_group(user, i.id):
                list_of_message = list(Messages.objects.filter(room_id=i.id).values("username", "message", "date"))
                last_message = list_of_message[len(list_of_message)-1]
            else:
                last_message = {"error": "Enter to get information"}
        except:
            last_message = {}
        list_to_return.append({"id": i.id, "name": i.name, "last_message":  last_message})
    return {"rooms": list_to_return}


@database_sync_to_async
def check_room(room_id):
    if len(list(Rooms.objects.filter(id=room_id).values())) > 0:
        return True
    else:
        return False


@database_sync_to_async
def add_user_in_room_group(name, room_id):
    room_group = RoomUsers()
    room_group.room_id = room_id
    room_group.username = name
    room_group.save()


def check_user_in_room_group(name, room_id):
    try:
        print(list(RoomUsers.objects.filter(room_id=room_id).values("username")))
        if {"username": name} in list(RoomUsers.objects.filter(room_id=room_id).values("username")):
            return True
        else:
            return False
    except:
        return False