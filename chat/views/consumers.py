import time
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
import json
from chat.functions.users import get_user_by_token, last_login_save
from chat.functions.rooms import check_room, add_user_in_room_group
from chat.functions.messages_storage import save_in_messages_storage, getout_from_messages_storage


class ChatConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.room_name = None

    async def connect(self):
        try:
            for i in filter(lambda x: x[0] == b'authorization', self.scope['headers']):
                self.scope["user"] = await get_user_by_token(list(i)[1].decode().split(" ")[1])
                if self.scope["user"] is not None:
                    if await check_room(self.scope["url_route"]["kwargs"]["room_id"]):
                        self.room_name = self.scope["url_route"]["kwargs"]["room_id"]
                        self.room_group_name = f"id_{self.room_name}"
                        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
                        await last_login_save(name=self.scope["user"])
                        await add_user_in_room_group(name=self.scope["user"], room_id=self.room_name)
                        all_messages = await getout_from_messages_storage(
                            self.scope["url_route"]["kwargs"]["room_id"])
                        await self.accept()
                        if all_messages is not None:
                            await self.send(text_data=json.dumps({"messages": all_messages}))
                    else:
                        await self.close(reason="BadRequest")
                else:
                    await self.close(reason="Unauthorized")
        except:
            await self.close(reason="BadRequest")

    #

    async def disconnect(self, code):
        #await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        await self.close()

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username
        timing = time.time()
        await save_in_messages_storage(self.scope["url_route"]["kwargs"]["room_id"], username, message, timing)
        await last_login_save(name=self.scope["user"])
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "username": username,
                "message": message,
                "timing": timing
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        timing = event["timing"]
        await self.send(text_data=json.dumps({"messages": [{"username": username, "message": message, "date": timing}]}))



