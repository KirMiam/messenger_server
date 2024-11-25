from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from rest_framework.authtoken.models import Token
from chat.models import Rooms
from chat.messages_storage import save_in_messages_storage, getout_from_messages_storage


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.room_name = None

    @database_sync_to_async
    def get_user(self, token_key):
        try:
            return Token.objects.get(key=token_key).user
        except Token.DoesNotExist:
            return None

    @database_sync_to_async
    def get_rooms(self):
        try:
            return list(Rooms.objects.all().values())
        except:
            return None

    async def connect(self):
        try:
            for i in filter(lambda x: x[0] == b'authorization', self.scope['headers']):
                self.scope["user"] = await self.get_user(list(i)[1].decode().split(" ")[1])
                if self.scope["user"] is not None:
                    for j in await self.get_rooms():
                        if self.scope["url_route"]["kwargs"]["room_id"] in str(j["id"]):
                            self.room_name = self.scope["url_route"]["kwargs"]["room_id"]
                            self.room_group_name = f"id_{self.room_name}"
                            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
                            print("1")
                            all_messages = await getout_from_messages_storage(self.scope["url_route"]["kwargs"]["room_id"])
                            print(all_messages)
                            await self.send_db(all_messages)
                            print("3")
                            await self.accept()
        except:
            await self.close(code=403)

    #

    async def disconnect(self, code):
        #await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username
        await save_in_messages_storage(self.scope["url_route"]["kwargs"]["room_id"], username, message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "username": username,
                "message": message,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        await self.send(text_data=json.dumps({"username": username, "message": message}))

    async def send_db(self, all_messages):
        await self.send(text_data=json.dumps({"messages": all_messages}))


