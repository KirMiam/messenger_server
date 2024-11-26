from django.urls import path
from chat.views import login, GetRooms, CreateRoom, registration, DeleteRoom, GetUsers
from client import views

urls_http = [
    # path(r'chat', views.index, name="index"),
    # path("chat/<str:room_name>/", views.room, name="room"),
    path(r'login', login),
    path(r'registration', registration),
    path(r'get_rooms', GetRooms.as_view()),
    path(r'create_room', CreateRoom.as_view()),
    path(r'delete_room', DeleteRoom.as_view()),
    path(r'get_users', GetUsers.as_view()),
    # path(r'test', test_func)
]
