from django.urls import path
from chat.views import login, Rooms, CreateRoom, registration
from client import views

urls_http = [
    # path(r'chat', views.index, name="index"),
    # path("chat/<str:room_name>/", views.room, name="room"),
    path(r'login', login),
    path(r'registration', registration),
    path(r'get_rooms', Rooms.as_view()),
    path(r'create_room', CreateRoom.as_view()),
    # path(r'test', test_func)
]
