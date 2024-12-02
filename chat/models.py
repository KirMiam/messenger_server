from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=30)


class Messages(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    message = models.CharField(max_length=100)
    date = models.FloatField(max_length=50)


class RoomUsers(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)