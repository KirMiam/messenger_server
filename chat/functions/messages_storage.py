from channels.db import database_sync_to_async
from chat.models import Rooms, Messages


@database_sync_to_async
def save_in_messages_storage(id_room, user, message, timing):
    mess = Messages()
    mess.room_id = id_room
    mess.username = user
    mess.message = message
    mess.date = timing
    if len(Messages.objects.filter(room_id=id_room).values()) > 50:
        Messages.objects.all()[0].delete()
    mess.save()


@database_sync_to_async
def getout_from_messages_storage(id_room):
    mess_store = list(Messages.objects.filter(room_id=id_room).values())
    if len(mess_store) > 0:
        return mess_store
    else:
        return None