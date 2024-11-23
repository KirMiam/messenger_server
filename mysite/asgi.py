from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from django.core.asgi import get_asgi_application
from chat.ws_urls import urls_ws
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(urls_ws)
    )
})
