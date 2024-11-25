from channels.db import database_sync_to_async
from chat.models import MessagesStorage


@database_sync_to_async
def save_in_messages_storage(id_room, message):
    storage = MessagesStorage()
    try:
        if len(MessagesStorage.objects.filter(id_room=id_room).values()) == 0:
            storage.id_room = id_room
            storage.save()
            print(MessagesStorage.objects.all())
        else:
            print("error2")
            return None
    except:
        print("error1")
        return None