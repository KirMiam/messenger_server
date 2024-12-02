from django.urls import include, path
from chat.http_urls import urls_http
from chat.ws_urls import urls_ws

urlpatterns = [
    path("", include(urls_http)),
    path("ws", include(urls_ws)),
]
