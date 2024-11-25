from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=30)

class MessagesStorage(models.Model):
    name = models.CharField(max_length=30)