from django.urls import re_path
from chat.consumers import ChatConsumer

urls_ws = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", ChatConsumer.as_asgi())
]
