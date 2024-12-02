from django.urls import path
from chat.views.views_users import login, GetRooms, CreateRoom, registration, DeleteRoom, GetUsers
from chat.views.views_admin import GetRoomsAdmin

urls_http = [
    # path(r'chat', views.index, name="index"),
    # path("chat/<str:room_name>/", views.room, name="room"),
    path(r'login', login),
    path(r'registration', registration),
    path(r'get_rooms', GetRooms.as_view()),
    path(r'create_rooms', CreateRoom.as_view()),
    path(r'delete_rooms', DeleteRoom.as_view()),
    path(r'get_users', GetUsers.as_view()),
    path(r'get_superusers', GetRoomsAdmin.as_view()),
]
