from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from asgiref.sync import sync_to_async
from chat.models import Rooms


class ChatConsumer(AsyncWebsocketConsumer):

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
                        if self.scope["url_route"]["kwargs"]["room_name"] in j["name"]:
                            self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
                            self.room_group_name = f"chat_{self.room_name}"
                            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
                            await self.accept()
        except:
            await self.close(code=403)

    #

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # await self.send(text_data=json.dumps({"message": message}))
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
        #print("send message")



