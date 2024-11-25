import time

from channels.db import database_sync_to_async
from chat.models import Rooms, Message
import datetime


@database_sync_to_async
def save_in_messages_storage(id_room, user, message):
    mess = Message()
    mess.username = user
    mess.message = message
    mess.time = time.time()
    room = Rooms.objects.get(id=id_room)
    room.group.append(mess.get())
    room.save()


@database_sync_to_async
def getout_from_messages_storage(id_room):
    room = Rooms.objects.get(id=id_room)
    print(room.group)
    return room.group["username"], room.group["message"], room.group["date"]

    # try:
    #     if len(storage) == 0:
    #         storage.name = id_room
    #         storage.save()
    #         Membership.objects.create(person = user,group = storage)
    #     else:
    #         print("error2")
    #         return None
    # except:
    #     print("error1")
    #     return None